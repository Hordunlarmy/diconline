from datetime import datetime

from src.shared.database import Database, database
from src.shared.manager import BaseManager


class AssignmentManager(BaseManager):

    def __init__(self, db: Database = database):
        super().__init__(db)

    async def get_assignments(self, course_id=None):
        query = f"""
            SELECT 
                a.* 
            FROM {self.assignments_table} a
            WHERE a.course_id = %s
        """
        return self.db.select(query, (course_id,))

    async def get_assignment(self, assignment_id):
        query = f"""
            SELECT 
                a.*, 
                COALESCE(
                    JSON_AGG(
                        JSON_BUILD_OBJECT('id', acc.id, 'name', 
                        CONCAT(acc.first_name, ' ', acc.last_name))
                    ) FILTER (WHERE acc.id IS NOT NULL), 
                    '[]'::JSON
                ) AS students
            FROM {self.assignments_table} a
            LEFT JOIN {self.assignment_submissions_table} as_sub 
                ON as_sub.assignment_id = a.id
            LEFT JOIN {self.accounts_table} acc 
                ON acc.id = as_sub.student_id
            WHERE a.id = %s
            GROUP BY a.id
        """
        return self.db.select(query, (assignment_id,))

    async def create_assignment(self, data):
        course_id = data.get("course_id")
        title = data.get("title", None)
        description = data.get("description", None)
        due_date = data.get("due_date", datetime.now())
        assignment_url = data.get("assignment_url", None)
        pass_mark = data.get("pass_mark", 70)

        query = f"""
            INSERT INTO {self.assignments_table} 
            (course_id, title, description, due_date, assignment_url,
            pass_mark)
            VALUES (%s, %s, %s, %s, %s, %s)
            RETURNING id
            """

        return self.db.commit(
            query,
            (
                course_id,
                title,
                description,
                due_date,
                assignment_url,
                pass_mark,
            ),
        )

    async def update_assignment(self, assignment_id, data):
        title = data.get("title", None)
        description = data.get("description", None)
        due_date = data.get("due_date", None)
        assignment_url = data.get("assignment_url", None)
        pass_mark = data.get("pass_mark", None)

        query = f"""
            UPDATE {self.assignments_table}
            SET title = %s, description = %s, due_date = %s,
            assignment_url = %s,
            pass_mark = %s
            WHERE id = %s
            """

        return self.db.update(
            query,
            (
                title,
                description,
                due_date,
                assignment_url,
                pass_mark,
                assignment_id,
            ),
        )

    async def delete_assignment(self, assignment_id):
        query = f"""
            DELETE FROM {self.assignments_table}
            WHERE id = %s
            """
        return self.db.delete(query, (assignment_id,))

    async def get_assignment_submissions(self, assignment_id):
        query = f"""
            SELECT 
                a.*, 
                COALESCE(
                    JSON_AGG(
                        JSON_BUILD_OBJECT('id', acc.id, 'name', 
                        CONCAT(acc.first_name, ' ', acc.last_name))
                    ) FILTER (WHERE acc.id IS NOT NULL), 
                    '[]'::JSON
                ) AS submissions
            FROM {self.assignments_table} a
            LEFT JOIN {self.assignment_submissions_table} as_sub 
                ON as_sub.assignment_id = a.id
            LEFT JOIN {self.accounts_table} acc 
                ON acc.id = as_sub.student_id
            WHERE a.id = %s
            GROUP BY a.id
        """
        return self.db.select(query, (assignment_id,))
