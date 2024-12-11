from src.shared.database import Database, database
from src.shared.manager import BaseManager


class StaffManager(BaseManager):
    def __init__(self, db: Database = database):
        super().__init__(db)

    async def get_staff(self, staff_id):
        query = f"""
            SELECT a.id, a.first_name, a.last_name, a.email, a.phone_number,
                a.state, a.local_government, d.name AS department
            FROM {self.accounts_table} a
            LEFT JOIN {self.staffs_table} s ON a.id = s.account_id
            LEFT JOIN {self.departments_table} d ON d.id = s.department_id
            WHERE a.id = %s AND a.account_type_id = 2
        """

        return self.db.select(query, (staff_id,))

    async def get_staffs(self, data):
        page = data.get("page", 1)
        page_size = data.get("page_size", 10)
        status_filter = data.get("status", None)
        order_by = data.get("order_by", "created_at") or "created_at"
        sort_by = data.get("sort_by", "DESC") or "DESC"

        offset = (page - 1) * page_size

        query = f"""
            SELECT a.id, a.first_name, a.last_name, a.email, a.phone_number,
                a.state, a.local_government, a.created_at,
                d.name AS department
            FROM {self.accounts_table} a
            LEFT JOIN {self.staffs_table} s ON a.id = s.account_id
            LEFT JOIN {self.departments_table} d ON d.id = s.department_id
            WHERE a.account_type_id = 2
        """

        if status_filter:
            query += f" AND s.status = '{status_filter}'"

        query += (
            f" ORDER BY {order_by} {sort_by} LIMIT {page_size} OFFSET {offset}"
        )

        data_result = self.db.select(query)
        total_count = await self._get_staffs_count(status_filter)

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

    async def get_staff_courses(self, lecturer_id):
        query = f"""
            SELECT *
            FROM {self.courses_table}
            WHERE lecturer_id = %s
        """

        return self.db.select(query, (lecturer_id,))
