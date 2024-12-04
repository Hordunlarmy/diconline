from src.shared.database import Database, database
from src.shared.manager import BaseManager


class ProgramManager(BaseManager):

    def __init__(self, db: Database = database):
        super().__init__(db)

    async def get_programs(self):
        query = f"SELECT * FROM {self.programs_table}"
        return self.db.select(query)

    async def get_program(self, program_id):
        query = f"SELECT * FROM {self.programs_table} WHERE id = %s"
        return self.db.select(query, (program_id,))
