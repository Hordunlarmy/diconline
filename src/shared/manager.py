from src.shared.database import Database, database


class BaseManager:

    def __init__(self, db: Database = database):
        self.db = db
        self.departments_table = "dic_departments"
        self.programs_table = "dic_programs"
        self.courses_table = "dic_courses"
        self.applications_table = "dic_applications"
        self.courses_enrollments_table = "dic_courses_enrollments"
        self.course_videos_table = "dic_course_videos"
        self.students_table = "dic_students"
        self.accounts_table = "dic_accounts"
        self.staffs_table = "dic_staffs"
        self.batches_table = "dic_batches"

    async def _get_applications_count(self, status_filter=None):
        count_query = f"""
            SELECT COUNT(*) AS count
            FROM {self.applications_table} a
        """

        if status_filter:
            count_query += f" WHERE a.status = '{status_filter}'"

        count_result = self.db.select(count_query)
        return count_result[0]["count"] if count_result else 0

    async def _get_students_count(self, status_filter=None):
        count_query = f"""
            SELECT COUNT(*)
            FROM {self.students_table} s
            LEFT JOIN {self.accounts_table} a ON a.id = s.account_id
            LEFT JOIN {self.departments_table} d ON d.id = s.department_id
        """

        if status_filter:
            count_query += f" WHERE s.status = '{status_filter}'"

        count_result = self.db.select(count_query)
        return count_result[0]["count"] if count_result else 0
