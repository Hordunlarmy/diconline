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
        LEFT JOIN {self.courses_table} c ON c.program_id = p.id
        GROUP BY d.id
        """
        return self.db.select(query)

    async def get_department(self, department_id):
        query = f"SELECT * FROM {self.departments_table} WHERE id = %s"
        return self.db.select(query, (department_id,))