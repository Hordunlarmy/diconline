from src.shared.database import Database, database
from src.shared.manager import BaseManager


class ProgramManager(BaseManager):

    def __init__(self, db: Database = database):
        super().__init__(db)

    async def get_programs(self, department_id=None):
        query = f"SELECT * FROM {self.programs_table}"
        query = f"""
        SELECT 
            p.*, 
            COUNT(DISTINCT c.id) AS total_courses
        FROM {self.programs_table} p
        LEFT JOIN {self.courses_table} c ON c.program_id = p.id
        WHERE p.department_id = %s
        GROUP BY p.id
        """

        return self.db.select(query, (department_id,))

    async def get_all_programs(self):
        query = f"SELECT * FROM {self.programs_table}"
        return self.db.select(query)

    async def get_program(self, program_id):
        query = f"SELECT * FROM {self.programs_table} WHERE id = %s"
        return self.db.select(query, (program_id,))
