from src.shared.database import Database, database
from src.shared.manager import BaseManager


class StudentManager(BaseManager):

    def __init__(self, db: Database = database):
        super().__init__(db)

    async def get_students(self, data):
        page = data.get("page", 1)
        page_size = data.get("page_size", 10)
        status_filter = data.get("status", None)
        sort_by = data.get("sort_by", "created_at")
        order_by = data.get("order_by", "ASC")

        sort_by_map = {
            "id": "s.id",
            "created_at": "s.created_at",
            "enrollment_date": "s.enrollment_date",
            "first_name": "a.first_name",
            "last_name": "a.last_name",
            "department": "d.name",
            "status": "s.status",
        }

        if sort_by:
            sort_by = sort_by_map.get(sort_by.lower(), "s.created_at")
        else:
            sort_by = "s.created_at"

        if order_by not in ["ASC", "DESC"]:
            order_by = "ASC"

            offset = (page - 1) * page_size

            query = f"""
                SELECT
                    s.id,
                    CONCAT(a.first_name, ' ', a.last_name) AS name,
                    d.name AS department,
                    a.phone_number,
                    s.created_at::DATE AS enrollment_date
                FROM {self.students_table} s
                LEFT JOIN {self.accounts_table} a ON a.id = s.account_id
                LEFT JOIN {self.programs_table} p ON p.id = s.program_id
                LEFT JOIN {self.departments_table} d ON d.id = p.department_id
            """

            if status_filter:
                query += f" WHERE s.status = '{status_filter}'"

            query += f" ORDER BY {sort_by} {order_by}"
            query += f" LIMIT {page_size} OFFSET {offset}"

            data_result = self.db.select(query)
            total_count = await self._get_students_count(status_filter)

            return await self._pagination_response(
                data_result, total_count, page, page_size
            )

    async def get_student_profile(self, student_id):
        query = f"""
            WITH exam_stats AS (
                SELECT
                    s.id AS student_id,
                    COUNT(DISTINCT e.id) AS total_exams,
                    COUNT(DISTINCT er.id) AS attempted_exams,
                    COUNT(DISTINCT CASE WHEN 
                        er.score >= e.pass_mark THEN er.id END) 
                        AS passed_exams,
                    COUNT(DISTINCT CASE WHEN 
                        er.score < e.pass_mark THEN er.id END) 
                        AS failed_exams
                FROM {self.students_table} s
                LEFT JOIN {self.programs_table} p ON p.id = s.program_id
                LEFT JOIN {self.programs_courses_table} pc 
                    ON pc.program_id = p.id
                LEFT JOIN {self.exams_table} e ON e.course_id = pc.course_id
                LEFT JOIN {self.exam_results_table} er 
                    ON er.exam_id = e.id AND er.student_id = s.id
                WHERE s.id = %s
                GROUP BY s.id
            ),
            assignment_stats AS (
                SELECT
                    s.id AS student_id,
                    COUNT(DISTINCT asm.id) AS total_assignments,
                    COUNT(DISTINCT asub.id) AS submitted_assignments,
                    COUNT(DISTINCT CASE WHEN asub.score >= asm.pass_mark 
                        THEN asub.id END) 
                        AS passed_assignments,
                    COUNT(DISTINCT CASE WHEN asub.score < asm.pass_mark 
                        THEN asub.id END) 
                        AS failed_assignments
                FROM {self.students_table} s
                LEFT JOIN {self.programs_table} p ON p.id = s.program_id
                LEFT JOIN {self.programs_courses_table} pc 
                    ON pc.program_id = p.id
                LEFT JOIN {self.assignments_table} asm 
                    ON asm.course_id = pc.course_id
                LEFT JOIN {self.assignment_submissions_table} asub 
                    ON asub.assignment_id = asm.id AND asub.student_id = s.id
                WHERE s.id = %s
                GROUP BY s.id
            )
            SELECT DISTINCT ON (s.id)
                s.id AS student_id,
                d.name AS department,
                d.head_of_department,
                dg.name AS degree,
                TO_CHAR(d.created_at, 'DD Mon YYYY') AS department_created_on,
                CONCAT(d.name, ' ', dg.name) AS program,
                a.first_name || ' ' || a.last_name AS full_name,
                s.next_of_kin_name AS next_of_kin,
                TO_CHAR(p.created_at, 'DD Mon YYYY') AS program_start,
                TO_CHAR(p.created_at + INTERVAL '1 year', 'DD Mon YYYY') 
                    AS program_end,
                a.state,
                a.local_government,
                a.address,
                a.phone_number,
                a.email,
                JSON_BUILD_OBJECT(
                    'total_exams', es.total_exams,
                    'attempted_exams', es.attempted_exams,
                    'passed_exams', es.passed_exams,
                    'failed_exams', es.failed_exams
                ) AS exam_stats,
                JSON_BUILD_OBJECT(
                    'total_assignments', ast.total_assignments,
                    'submitted_assignments', ast.submitted_assignments,
                    'passed_assignments', ast.passed_assignments,
                    'failed_assignments', ast.failed_assignments
                ) AS assignment_stats

            FROM {self.accounts_table} a
            LEFT JOIN {self.students_table} s ON s.account_id = a.id
            LEFT JOIN {self.programs_table} p ON p.id = s.program_id
            LEFT JOIN {self.programs_courses_table} pc ON pc.program_id = p.id
            LEFT JOIN {self.departments_table} d ON d.id = p.department_id
            LEFT JOIN {self.degrees_table} dg ON dg.id = p.degree_id
            LEFT JOIN exam_stats es ON es.student_id = s.id
            LEFT JOIN assignment_stats ast ON ast.student_id = s.id

            WHERE s.id = %s
            ORDER BY s.id, p.created_at DESC
        """
        return self.db.select(query, (student_id, student_id, student_id))

    async def get_student_courses(self, student_id):
        query = f"""
            SELECT
                c.id AS course_id,
                c.name AS course_name,
                COUNT(cv.id) AS total_videos
            FROM {self.courses_table} c
            LEFT JOIN {self.courses_enrollments_table} ce 
                ON ce.course_id = c.id
            LEFT JOIN {self.course_videos_table} cv ON cv.course_id = c.id
            WHERE ce.student_id = %s
            GROUP BY c.id, c.name
        """
        return self.db.select(query, (student_id,))

    async def get_student_exams(self, student_id):
        query = f"""
            SELECT
                e.id AS exam_id,
                d.name AS department,
                c.name AS course,
                TO_CHAR(e.start_date, 'DD-MM-YYYY') AS exam_date,
                CONCAT(
                    TO_CHAR(e.start_date, 'HH12:MI AM'), ' - ',
                    TO_CHAR(
                        e.start_date + (e.duration || ' minutes')::INTERVAL,
                        'HH12:MI AM'
                    )
                ) AS time_range,
                ROUND((e.pass_mark::FLOAT / e.duration * 100)::NUMERIC, 2)
                    AS passing_percentage,
                COUNT(er.id) AS total_attempts,
                COALESCE(
                    ROUND(AVG(er.score)::NUMERIC, 2),
                    0
                ) AS scored_percentage
            FROM {self.exams_table} e
            LEFT JOIN {self.exam_results_table} er ON er.exam_id = e.id
            LEFT JOIN {self.students_table} s ON s.id = er.student_id
            LEFT JOIN {self.courses_table} c ON c.id = e.course_id
            LEFT JOIN {self.programs_table} p ON p.id = s.program_id
            LEFT JOIN {self.departments_table} d ON d.id = p.department_id

            WHERE er.student_id = %s
            GROUP BY e.id, e.title, e.start_date, e.duration, e.pass_mark,
            c.name, d.name
        """

        results = self.db.select(query, (student_id,))
        return results if results else []

    async def get_student_assignments(self, student_id):
        query = f"""
            SELECT
                a.id AS assignment_id,
                d.name AS department,
                c.name AS course,
                a.title AS assignment_title,
                TO_CHAR(a.created_at, 'DD-MM-YYYY') AS assigned_date,
                TO_CHAR(a.due_date, 'DD-MM-YYYY') AS due_date,
                TO_CHAR(a.due_date, 'HH12:MI AM') AS due_time,
                ROUND(
                    (a.pass_mark::FLOAT / 100 * 100)::NUMERIC,
                    2
                ) AS passing_percentage,
                COALESCE(
                    ROUND(AVG(asub.score)::NUMERIC, 2),
                    0
                ) AS scored_percentage
            FROM {self.assignments_table} a
            LEFT JOIN {self.assignment_submissions_table} asub 
                ON asub.assignment_id = a.id
            LEFT JOIN {self.students_table} s ON s.id = asub.student_id
            LEFT JOIN {self.courses_table} c ON c.id = a.course_id
            LEFT JOIN {self.programs_table} p ON p.id = s.program_id
            LEFT JOIN {self.departments_table} d ON d.id = p.department_id
            WHERE asub.student_id = %s
            GROUP BY a.id, a.title, a.due_date, a.pass_mark, c.name, d.name
        """

        results = self.db.select(query, (student_id,))
        return results if results else []

    async def get_student_exam_result(self, exam_id, student_id):
        query = f"""
            SELECT 
                er.id AS result_id,
                CONCAT(a.first_name, ' ', a.last_name) AS student_name,
                a.id AS student_id,
                c.name AS course_name,
                e.title AS exam_title,
                TO_CHAR(er.created_at, 'HH12:MI AM | DD Month YYYY') 
                AS result_date,
                er.score AS student_score,
                e.pass_mark AS passing_mark,
                ROUND((er.score::FLOAT / e.pass_mark * 100)::NUMERIC, 2) 
                    AS student_percentage,
                ROUND((e.pass_mark::FLOAT / e.duration * 100)::NUMERIC, 2) 
                    AS passing_percentage,
                e.question_paper_url AS question_paper_url,
                er.student_submission_url AS student_response_url
            FROM {self.exam_results_table} er
            LEFT JOIN {self.accounts_table} a ON a.id = er.student_id
            LEFT JOIN {self.exams_table} e ON e.id = er.exam_id
            LEFT JOIN {self.courses_table} c ON c.id = e.course_id
            WHERE er.exam_id = %s AND er.student_id = %s
        """
        results = self.db.select(query, (exam_id, student_id))
        return results if results else []

    async def submit_assignment(self, student_id, data):
        assignment_id = data.get("assignment_id")
        submission = data.get("submission_url")

        query = f"""
            INSERT INTO {self.assignment_submissions_table} 
            (student_id, assignment_id, submission_url)
            VALUES (%s, %s, %s)
            RETURNING id
        """
        return self.db.commit(
            query,
            (student_id, assignment_id, submission),
        )
