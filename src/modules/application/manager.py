import random
import string

from decouple import config

from src.shared.auth import get_password_hash
from src.shared.database import Database, database
from src.shared.email import sender
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

        filter_condition = (
            f"a.status = '{status_filter}'" if status_filter else None
        )

        total_count = await self._get_count(
            self.applications_table,
            filter_condition=filter_condition,
        )

        return await self._pagination_response(
            data_result, total_count, page, page_size
        )

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
        result = self.db.select(query, (application_id,))
        return result[0] if result else None

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

    async def approve_application(self, application_id):
        approve_query = f"""
            UPDATE {self.applications_table}
            SET status = 'Approved'
            WHERE id = %s
        """
        self.db.commit(approve_query, (application_id,))

        application = await self.get_application(application_id)
        if application:
            application = application[0]
        else:
            raise ValueError("Application not found")

        password = self.generate_password()

        create_account_query = f"""
            INSERT INTO {self.accounts_table}
            (photo_url, first_name, last_name, email, phone_number, gender, 
             account_type_id, password, date_of_birth)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
            RETURNING id
        """
        account_data = (
            application["photo_url"],
            application["first_name"],
            application["last_name"],
            application["email"],
            application["phone_number"],
            application["gender"],
            1,
            get_password_hash(password),
            application["date_of_birth"],
        )

        account_id = self.db.commit(create_account_query, account_data)

        print(account_id)

        create_student_query = f"""
            INSERT INTO {self.students_table}
            (account_id, batch_id, program_id)
            VALUES (%s, %s, %s);
        """
        student_data = (
            account_id,
            6,
            application["program_id"],
        )

        self.db.commit(create_student_query, student_data)

        template_variables = {
            "name": f"{application['first_name']} {application['last_name']}",
            "email": application["email"],
            "password": password,
            "login_link": config("LOGIN_URL"),
        }

        sender.send_login_details(
            recipient_email=application["email"],
            recipient_name=template_variables["name"],
            template_variables=template_variables,
        )

        return {"email": application["email"], "password": password}

    def generate_password(self, length=12):

        characters = string.ascii_letters + string.digits + string.punctuation
        return "".join(random.choices(characters, k=length))
