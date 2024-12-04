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

    async def get_student_dashboard(self, student_id):
        query = f"""
            -- Get current year data
            WITH current_year_data AS (
                SELECT 
                    COUNT(DISTINCT CASE WHEN s.status = 'Active' THEN s.id END) AS active_students,
                    COUNT(DISTINCT CASE WHEN s.status = 'Dropout' THEN s.id END) AS dropout_students,
                    COUNT(DISTINCT s.id) AS total_students
                FROM {self.students_table} s
                WHERE EXTRACT(YEAR FROM s.created_at) = EXTRACT(YEAR FROM CURRENT_DATE)
            ),

            -- Get previous year data
            previous_year_data AS (
                SELECT 
                    COUNT(DISTINCT CASE WHEN s.status = 'Active' THEN s.id END) AS active_students,
                    COUNT(DISTINCT CASE WHEN s.status = 'Dropout' THEN s.id END) AS dropout_students,
                    COUNT(DISTINCT s.id) AS total_students
                FROM {self.students_table} s
                WHERE EXTRACT(YEAR FROM s.created_at) = EXTRACT(YEAR FROM CURRENT_DATE) - 1
            )

            -- Main query to calculate current and percentage increase
            SELECT 
                current_year_data.active_students,
                current_year_data.dropout_students,
                current_year_data.total_students,
                
                -- Active students percentage increase
                COALESCE(
                    (current_year_data.active_students - previous_year_data.active_students) 
                    * 100.0 / NULLIF(previous_year_data.active_students, 0), 0
                ) AS active_students_percentage_increase,

                -- Dropout students percentage increase
                COALESCE(
                    (current_year_data.dropout_students - previous_year_data.dropout_students) 
                    * 100.0 / NULLIF(previous_year_data.dropout_students, 0), 0
                ) AS dropout_students_percentage_increase,

                -- Total students percentage increase
                COALESCE(
                    (current_year_data.total_students - previous_year_data.total_students) 
                    * 100.0 / NULLIF(previous_year_data.total_students, 0), 0
                ) AS total_students_percentage_increase

            FROM current_year_data, previous_year_data
        """
        return self.db.select(query, (student_id, student_id))
