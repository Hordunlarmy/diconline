from src.shared.database import Database, database
from src.shared.file_handler import upload_file
from src.shared.manager import BaseManager


class ApplicationManager(BaseManager):

    def __init__(self, db: Database = database):
        super().__init__(db)

    async def get_applications(self):
        query = f"SELECT * FROM {self.applications_table}"
        return self.db.select(query)

    async def get_application(self, application_id):
        query = f"SELECT * FROM {self.applications_table} WHERE id = %s"
        return self.db.select(query, (application_id,))

    async def create_application(self, data):
        if data["photo"]:
            photo_url = await upload_file(data["photo"], folder="photos")

        if data["application_form"]:
            application_form_url = await upload_file(
                data["application_form"], folder="application_forms"
            )

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
