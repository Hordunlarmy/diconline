from src.shared.database import Database, database
from src.shared.manager import BaseManager


class DashboardManager(BaseManager):

    def __init__(self, db: Database = database):
        super().__init__(db)

    async def get_dashboard(self):
        query = f"""
            SELECT 
                (SELECT COUNT(*) FROM {self.applications_table}
                    WHERE status = 'Pending') AS pending_applications,
                COUNT(DISTINCT CASE WHEN s.status = 'Active' THEN s.id END)
                    AS active_students,
                COUNT(DISTINCT CASE WHEN st.status = 'Active' THEN st.id END)
                    AS active_staffs,
                COUNT(DISTINCT c.id) AS total_courses
            FROM {self.accounts_table} ac
            LEFT JOIN {self.students_table} s ON s.account_id = ac.id
            LEFT JOIN {self.staffs_table} st ON st.account_id = ac.id
            LEFT JOIN {self.programs_table} p ON p.id = s.program_id
            LEFT JOIN {self.departments_table} d ON d.id = p.department_id
            LEFT JOIN {self.programs_courses_table} pc ON pc.program_id = p.id 
            LEFT JOIN {self.courses_table} c ON c.id = pc.course_id
        """
        return self.db.select(query)

    async def get_department_dashboard(self, data):
        page = data.get("page", 1)
        page_size = data.get("page_size", 10)

        offset = (page - 1) * page_size

        query = f"""
            SELECT 
                d.name AS department_name,
                COUNT(DISTINCT s.id) AS total_students
            FROM {self.departments_table} d
            LEFT JOIN {self.programs_table} p ON p.department_id = d.id
            LEFT JOIN {self.students_table} s ON s.program_id = p.id
            GROUP BY d.name
            LIMIT {page_size} OFFSET {offset}
        """

        data = self.db.select(query)

        count_query = f"""
            SELECT COUNT(DISTINCT d.id)
            FROM {self.departments_table} d
            LEFT JOIN {self.programs_table} p ON p.department_id = d.id
            LEFT JOIN {self.students_table} s ON s.program_id = p.id
        """
        result = self.db.select(count_query)
        total_count = result[0]["count"] if result else 0

        return await self._pagination_response(
            data, total_count, page, page_size
        )

    async def get_staff_dashboard(self):
        count_query = f"""
            SELECT 
                COUNT(*) FILTER (WHERE r.role = 'teaching') 
                    AS teaching_staffs,
                COUNT(*) FILTER (WHERE r.role = 'non-teaching') 
                    AS non_teaching_staffs,
                COUNT(*) AS total_staff
            FROM {self.staffs_table} s
            JOIN {self.staff_roles_table} r ON s.role_id = r.id
        """
        result = self.db.select(count_query)

        return result[0] if result else {}

    async def get_student_dashboard(self, student_id):
        query = f"""
            -- Get current year data
            WITH current_year_data AS (
                SELECT 
                    COUNT(DISTINCT CASE WHEN s.status = 'Active' THEN s.id END) AS active_students,
                    COUNT(DISTINCT CASE WHEN s.status = 'Dropout' THEN s.id END) AS dropout_students,
                    COUNT(DISTINCT s.id) AS total_students
                FROM {self.students_table} s
                WHERE EXTRACT(YEAR FROM s.created_at) = EXTRACT(YEAR FROM CURRENT_DATE)
            ),

            -- Get previous year data
            previous_year_data AS (
                SELECT 
                    COUNT(DISTINCT CASE WHEN s.status = 'Active' THEN s.id END) AS active_students,
                    COUNT(DISTINCT CASE WHEN s.status = 'Dropout' THEN s.id END) AS dropout_students,
                    COUNT(DISTINCT s.id) AS total_students
                FROM {self.students_table} s
                WHERE EXTRACT(YEAR FROM s.created_at) = EXTRACT(YEAR FROM CURRENT_DATE) - 1
            )

            -- Main query to calculate current and percentage increase
            SELECT 
                current_year_data.active_students,
                current_year_data.dropout_students,
                current_year_data.total_students,
                
                -- Active students percentage increase
                COALESCE(
                    (current_year_data.active_students - previous_year_data.active_students) 
                    * 100.0 / NULLIF(previous_year_data.active_students, 0), 0
                ) AS active_students_percentage_increase,

                -- Dropout students percentage increase
                COALESCE(
                    (current_year_data.dropout_students - previous_year_data.dropout_students) 
                    * 100.0 / NULLIF(previous_year_data.dropout_students, 0), 0
                ) AS dropout_students_percentage_increase,

                -- Total students percentage increase
                COALESCE(
                    (current_year_data.total_students - previous_year_data.total_students) 
                    * 100.0 / NULLIF(previous_year_data.total_students, 0), 0
                ) AS total_students_percentage_increase

            FROM current_year_data, previous_year_data
        """
        return self.db.select(query, (student_id, student_id))
