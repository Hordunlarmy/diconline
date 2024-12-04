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
