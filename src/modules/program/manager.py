from src.shared.database import Database, database
from src.shared.manager import BaseManager


class ProgramManager(BaseManager):

    def __init__(self, db: Database = database):
        super().__init__(db)

    async def get_programs(self, department_id=None):
        query = f"""
            SELECT 
                p.id, CONCAT(d.name, ' ', dg.name) AS program,
                p.degree_id, p.department_id, 
                COUNT(DISTINCT pc.course_id) AS total_courses
            FROM {self.programs_table} p
            LEFT JOIN {self.departments_table} d ON d.id = p.department_id
            LEFT JOIN {self.degrees_table} dg ON dg.id = p.degree_id
            LEFT JOIN {self.programs_courses_table} pc ON pc.program_id = p.id
            LEFT JOIN {self.courses_table} c ON c.id = pc.course_id
            WHERE p.department_id = %s
            GROUP BY p.id, d.name, dg.name
        """
        return self.db.select(query, (department_id,))

    async def get_all_programs(self):
        query = f"""
            SELECT p.id, CONCAT(d.name, ' ', dg.name) AS program,
                p.degree_id, p.department_id 
            FROM {self.programs_table} p
            JOIN {self.departments_table} d ON d.id = p.department_id
            JOIN {self.degrees_table} dg ON dg.id = p.degree_id
            ORDER BY program
        """
        return self.db.select(query)

    async def get_program(self, program_id):
        query = f"""
            SELECT 
                p.id, CONCAT(d.name, ' ', dg.name) AS program,
                p.degree_id, p.department_id 
            FROM {self.programs_table} p
            JOIN {self.departments_table} d ON d.id = p.department_id
            JOIN {self.degrees_table} dg ON dg.id = p.degree_id
            WHERE p.id = %s
        """
        return self.db.select(query, (program_id,))
