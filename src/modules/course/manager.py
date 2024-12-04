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
            COUNT(DISTINCT ce.id) AS total_students_enrolled
        FROM {self.courses_table} c
        LEFT JOIN {self.course_videos_table} cv ON cv.course_id = c.id
        LEFT JOIN {self.courses_enrollments_table} ce ON ce.course_id = c.id
        WHERE c.program_id = %s
        GROUP BY c.id, c.name, c.description, c.created_at, c.updated_at
        """

        return self.db.select(query, (program_id,))

    async def get_course(self, course_id):
        query = f"SELECT * FROM {self.courses_table} WHERE id = %s"
        return self.db.select(query, (course_id,))
