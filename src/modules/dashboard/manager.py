from src.shared.database import Database, database
from src.shared.manager import BaseManager


class DashboardManager(BaseManager):

    def __init__(self, db: Database = database):
        super().__init__(db)

    async def get_dashboard(self):
        query = f"""
            SELECT 
                (SELECT COUNT(*) FROM {self.applications_table}
                    WHERE status = 'Pending') AS pending_applications,
                COUNT(DISTINCT CASE WHEN s.status = 'Active' THEN s.id END)
                    AS active_students,
                COUNT(DISTINCT CASE WHEN st.status = 'Active' THEN st.id END)
                    AS active_staffs,
                COUNT(DISTINCT c.id) AS total_courses
            FROM {self.accounts_table} ac
            LEFT JOIN {self.students_table} s ON s.account_id = ac.id
            LEFT JOIN {self.staffs_table} st ON st.account_id = ac.id
            LEFT JOIN {self.departments_table} d ON d.id = s.department_id
            LEFT JOIN {self.programs_table} p ON p.department_id = d.id
            LEFT JOIN {self.courses_table} c ON c.program_id = p.id
        """
        return self.db.select(query)
