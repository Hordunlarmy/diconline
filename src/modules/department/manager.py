from src.shared.database import Database, database
from src.shared.manager import BaseManager


class DepartmentManager(BaseManager):

    def __init__(self, db: Database = database):
        super().__init__(db)

    async def get_departments(self):
        query = f"""
            SELECT 
                d.*, 
                COUNT(DISTINCT p.id) AS total_programs, 
                COUNT(DISTINCT c.id) AS total_courses
            FROM {self.departments_table} d
            LEFT JOIN {self.programs_table} p ON p.department_id = d.id
            LEFT JOIN {self.programs_courses_table} pc ON pc.program_id = p.id
            LEFT JOIN {self.courses_table} c ON c.id = pc.course_id
            GROUP BY d.id
            """
        return self.db.select(query)

    async def get_department(self, department_id):
        query = f"""
            SELECT 
                d.*, 
                COALESCE(
                    JSON_AGG(
                        JSON_BUILD_OBJECT('id', p.id, 'name', p.name)
                    ) FILTER (WHERE p.id IS NOT NULL), 
                    '[]'::JSON
                ) AS programs
            FROM {self.departments_table} d
            LEFT JOIN {self.programs_table} p ON p.department_id = d.id
            WHERE d.id = %s
            GROUP BY d.id
            """
        return self.db.select(query, (department_id,))
