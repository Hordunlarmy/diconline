from src.shared.database import Database, database
from src.shared.manager import BaseManager


class StudentManager(BaseManager):

    def __init__(self, db: Database = database):
        super().__init__(db)

    async def get_students(self, data):
        page = data.get("page", 1)
        page_size = data.get("page_size", 10)
        status_filter = data.get("status", None)
        sort_by = data.get("sort_by", "created_at")
        order_by = data.get("order_by", "ASC")

        # Normalize incoming sort_by to lowercase for comparison
        sort_by_map = {
            "id": "s.id",
            "created_at": "s.created_at",
            "enrollment_date": "s.enrollment_date",
            "first_name": "a.first_name",
            "last_name": "a.last_name",
            "department": "d.name",
            "status": "s.status",
        }

        if sort_by:
            sort_by = sort_by_map.get(sort_by.lower(), "s.created_at")
        else:
            sort_by = "s.created_at"

        if order_by not in ["ASC", "DESC"]:
            order_by = "ASC"

            offset = (page - 1) * page_size

            query = f"""
                SELECT 
                    CONCAT(a.first_name, ' ', a.last_name) AS name,
                    d.name AS department,
                    a.phone_number,
                    s.created_at::DATE AS enrollment_date
                FROM {self.students_table} s
                LEFT JOIN {self.accounts_table} a ON a.id = s.account_id
                LEFT JOIN {self.departments_table} d ON d.id = s.department_id
            """

            if status_filter:
                query += f" WHERE s.status = '{status_filter}'"

            query += f" ORDER BY {sort_by} {order_by}"
            query += f" LIMIT {page_size} OFFSET {offset}"

            data_result = self.db.select(query)
            total_count = await self._get_students_count(status_filter)

            total_pages = (total_count // page_size) + (
                1 if total_count % page_size > 0 else 0
            )

            return {
                "data": data_result,
                "meta": {
                    "total": len(data_result),
                    "total_pages": total_pages,
                    "current_page": page,
                    "page_size": page_size,
                },
            }
