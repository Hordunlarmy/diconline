from src.shared.database import Database, database


class BaseManager:

    def __init__(self, db: Database = database):
        self.db = db
        self.departments_table = "dic_departments"
        self.programs_table = "dic_programs"
        self.courses_table = "dic_courses"
        self.applications_table = "dic_applications"
