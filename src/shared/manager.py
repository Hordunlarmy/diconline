from datetime import timedelta

from src.shared.auth import ACCESS_TOKEN_EXPIRE_MINUTES, login_user
from src.shared.database import Database, database


class BaseManager:

    def __init__(self, db: Database = database):
        self.db = db
        self.degrees_table = "dic_degrees"
        self.departments_table = "dic_departments"
        self.programs_table = "dic_programs"
        self.courses_table = "dic_courses"
        self.programs_courses_table = "dic_programs_courses"
        self.applications_table = "dic_applications"
        self.courses_enrollments_table = "dic_courses_enrollments"
        self.course_videos_table = "dic_course_videos"
        self.students_table = "dic_students"
        self.accounts_table = "dic_accounts"
        self.account_types_table = "dic_account_types"
        self.staffs_table = "dic_staffs"
        self.batches_table = "dic_batches"
        self.exams_table = "dic_exams"
        self.exam_results_table = "dic_exam_results"
        self.assignments_table = "dic_assignments"
        self.assignment_submissions_table = "dic_assignment_submissions"

    @staticmethod
    async def account_exists(
        db: Database = database, email=None, account_id=None
    ):
        query = """
            SELECT id, email, password, account_type_id
            FROM dic_accounts
        """

        if email:
            query += f" WHERE email = '{email}'"

        if account_id:
            query += f" WHERE id = '{account_id}'"

        result = db.select(query)

        return result[0] if result else None

    async def _with_accessToken(self, user_id, account_type):
        """
        Generate JWT for a user
        """

        remember_me = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        jwt = login_user(
            remember_me,
            data={
                "id": user_id,
                "account_type": account_type,
            },
        )
        return jwt

    async def _get_count(self, table, joins=None, filter_condition=None):
        count_query = f"""
            SELECT COUNT(*)
            FROM {table}
        """

        if joins:
            for join in joins:
                count_query += f" {join}"

        if filter_condition:
            count_query += f" WHERE {filter_condition}"

        count_result = self.db.select(count_query)
        return count_result[0]["count"] if count_result else 0

    async def _get_students_count(self, status_filter=None):
        count_query = f"""
            SELECT COUNT(*)
            FROM {self.students_table} s
            LEFT JOIN {self.accounts_table} a ON a.id = s.account_id
            LEFT JOIN {self.programs_table} p ON p.id = s.program_id
            LEFT JOIN {self.departments_table} d ON d.id = p.department_id
        """

        if status_filter:
            count_query += f" WHERE s.status = '{status_filter}'"

        count_result = self.db.select(count_query)
        return count_result[0]["count"] if count_result else 0

    async def _get_staffs_count(self, status_filter=None):
        count_query = f"""
            SELECT COUNT(*)
            FROM {self.staffs_table} s
            LEFT JOIN {self.accounts_table} a ON a.id = s.account_id
            LEFT JOIN {self.departments_table} d ON d.id = s.department_id
        """

        if status_filter:
            count_query += f" WHERE s.status = '{status_filter}'"

        count_result = self.db.select(count_query)
        return count_result[0]["count"] if count_result else 0

    async def _pagination_response(self, data, total_count, page, page_size):
        total_pages = (total_count // page_size) + (
            1 if total_count % page_size > 0 else 0
        )

        total_pages = max(total_pages, 1) if total_count > 0 else 0

        return {
            "data": data,
            "meta": {
                "total": total_count,
                "total_pages": total_pages,
                "current_page": page,
                "page_size": page_size,
            },
        }
