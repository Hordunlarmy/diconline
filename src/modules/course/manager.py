from src.shared.database import Database, database
from src.shared.manager import BaseManager


class CourseManager(BaseManager):

    def __init__(self, db: Database = database):
        super().__init__(db)

    async def get_courses(self, program_id=None):
        query = f"""
        SELECT 
            c.id,
            c.name,
            c.description,
            c.created_at,
            c.updated_at,
            COUNT(DISTINCT cv.id) AS total_videos,
            COUNT(DISTINCT ce.id) AS total_students_enrolled,
            pc.program_id
        FROM {self.courses_table} c
        LEFT JOIN {self.course_videos_table} cv ON cv.course_id = c.id
        LEFT JOIN {self.courses_enrollments_table} ce ON ce.course_id = c.id
        LEFT JOIN {self.programs_courses_table} pc ON pc.course_id = c.id
        WHERE pc.program_id = %s
        GROUP BY c.id, c.name, c.description, c.created_at, c.updated_at,
        pc.program_id
        """
        return self.db.select(query, (program_id,))

    async def get_course(self, course_id):
        query = f"""
        SELECT 
            c.id,
            c.name,
            c.description,
            c.created_at,
            c.updated_at,
            pc.program_id
        FROM {self.courses_table} c
        LEFT JOIN {self.programs_courses_table} pc ON pc.course_id = c.id
        WHERE c.id = %s
        """
        return self.db.select(query, (course_id,))

    async def get_course_with_students(self, course_id: int):
        query = f"""
        SELECT 
            c.id,
            c.name,
            c.description,
            c.created_at,
            c.updated_at,
            COUNT(DISTINCT cv.id) AS total_videos,
            JSON_AGG(
                JSON_BUILD_OBJECT(
                    'student_id', s.id,
                    'student_name', CONCAT(a.first_name, ' ', a.last_name)
                )
            ) AS students
        FROM {self.courses_table} c
        LEFT JOIN {self.course_videos_table} cv ON cv.course_id = c.id
        LEFT JOIN {self.courses_enrollments_table} ce ON ce.course_id = c.id
        LEFT JOIN {self.students_table} s ON ce.student_id = s.id
        LEFT JOIN {self.accounts_table} a ON s.account_id = a.id
        WHERE c.id = %s
        GROUP BY c.id, c.name, c.description, c.created_at, c.updated_at
        """
        return self.db.select(query, (course_id,))

    async def get_course_videos(self, course_id):
        query = f"""
        SELECT *
        FROM {self.course_videos_table}
        WHERE course_id = %s
        """
        return self.db.select(query, (course_id,))

    async def get_course_students(self, course_id):
        query = f"""
        SELECT 
            s.id,
            a.first_name,
            a.last_name
        FROM {self.students_table} s
        LEFT JOIN {self.accounts_table} a ON s.account_id = a.id
        LEFT JOIN {self.courses_enrollments_table} ce ON ce.student_id = s.id
        WHERE ce.course_id = %s
        """
        return self.db.select(query, (course_id,))

    async def add_course_video(self, data):
        course_id = data.get("course_id")
        video_url = data.get("video_url")
        title = data.get("title", None)
        description = data.get("description", None)

        query = f"""
        INSERT INTO {self.course_videos_table} (course_id, video_url, title, 
        description)
        VALUES (%s, %s, %s, %s)
        RETURNING id
        """
        return self.db.commit(
            query, (course_id, video_url, title, description)
        )
