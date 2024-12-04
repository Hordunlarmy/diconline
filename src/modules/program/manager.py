from src.shared.database import Database, database


class ProgramManager:

    def __init__(self, db: Database = database):
        self.db = db
        self.table = "dic_programs"

    async def get_programs(self):
        query = f"SELECT * FROM {self.table}"
        return self.db.select(query)

    async def get_program(self, program_id):
        query = f"SELECT * FROM {self.table} WHERE id = %s"
        return self.db.select(query, (program_id,))
