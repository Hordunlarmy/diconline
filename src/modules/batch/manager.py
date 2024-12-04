from src.shared.database import Database, database
from src.shared.manager import BaseManager


class BatchManager(BaseManager):

    def __init__(self, db: Database = database):
        super().__init__(db)

    async def get_batches(self):
        query = f"""
            SELECT 
                b.id,
                b.name,
                COUNT(DISTINCT c.id) AS total_courses
            FROM {self.batches_table} b
            LEFT JOIN {self.courses_table} c 
                ON EXTRACT(YEAR FROM c.created_at) <= b.year
            GROUP BY b.id
        """

        return self.db.select(query)
