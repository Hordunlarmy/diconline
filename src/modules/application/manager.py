from src.shared.database import Database, database
from src.shared.error_handler import CustomError
from src.shared.file_handler import upload_file
from src.shared.manager import BaseManager


class ApplicationManager(BaseManager):

    def __init__(self, db: Database = database):
        super().__init__(db)

    async def get_applications(self, data):
        page = data.get("page", 1)
        page_size = data.get("page_size", 10)
        status_filter = data.get("status", None)

        offset = (page - 1) * page_size

        query = f"""
            SELECT a.id, CONCAT(a.first_name, ' ', a.last_name) AS name,
                CONCAT(d.name, ' ', dg.name) AS program,
                dg.name AS degree, d.name AS department,
                a.phone_number, a.email,
                a.created_at::DATE AS application_date
            FROM {self.applications_table} a
            LEFT JOIN {self.programs_table} p ON p.id = a.program_id
            JOIN {self.departments_table} d ON d.id = p.department_id
            JOIN {self.degrees_table} dg ON dg.id = p.degree_id
        """

        if status_filter:
            query += f" WHERE a.status = '{status_filter}'"

        query += (
            f" ORDER BY a.created_at DESC LIMIT {page_size} OFFSET {offset}"
        )

        data_result = self.db.select(query)
        total_count = await self._get_applications_count(status_filter)

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

    async def get_application(self, application_id):
        query = f"""
            SELECT a.*, CONCAT(d.name, ' ', dg.name) AS program,
            dg.name AS degree, d.name AS department
            FROM {self.applications_table} a
            LEFT JOIN {self.programs_table} p ON p.id = a.program_id
            JOIN {self.departments_table} d ON d.id = p.department_id
            JOIN {self.degrees_table} dg ON dg.id = p.degree_id
            WHERE a.id = %s
            """
        return self.db.select(query, (application_id,))

    async def create_application(self, data):
        if data["photo"]:
            photo_url = await upload_file(data["photo"], folder="photos")
        else:
            raise CustomError("Photo is required", status_code=400)

        if data["application_form"]:
            application_form_url = await upload_file(
                data["application_form"], folder="application_forms"
            )
        else:
            raise CustomError("Application form is required", status_code=400)

        query = f"""
            INSERT INTO {self.applications_table} (
                first_name, last_name, email, phone_number, gender, 
                date_of_birth, program_id, photo_url, application_form_url
            ) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id
        """

        return self.db.commit(
            query,
            (
                data["first_name"],
                data["last_name"],
                data["email"],
                data["phone"],
                data["gender"],
                data["dob"],
                data["program_id"],
                photo_url,
                application_form_url,
            ),
        )
