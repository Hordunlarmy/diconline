from contextlib import contextmanager

import psycopg2
from decouple import config
from psycopg2 import Error


class Database:
    def __init__(self, database_url=None):
        self.database_url = database_url or config("DATABASE_URL")

    @contextmanager
    def _get_connection(self):
        connection = None
        try:
            connection = psycopg2.connect(self.database_url)
            yield connection
        except Error as e:
            print(f"Connection error: {e}")
            yield None
        finally:
            if connection:
                connection.close()

    def commit(self, query, params=None):
        with self._get_connection() as connection:
            if connection is None:
                print("Failed to get a database connection.")
                return False

            try:
                with connection.cursor() as cursor:
                    cursor.execute(query, params)
                    connection.commit()
                    return cursor.fetchone()[0] if cursor.description else None
            except Error as e:
                print(f"Commit error: {e}")
                connection.rollback()
                return False

    def select(self, query, params=None, format=True):
        with self._get_connection() as connection:
            if connection is None:
                print("Failed to get a database connection.")
                return False

            try:
                with connection.cursor() as cursor:
                    cursor.execute(query, params)
                    records = cursor.fetchall()
                    col_names = [desc[0] for desc in cursor.description]

                    return (
                        [dict(zip(col_names, record)) for record in records]
                        if format
                        else (col_names, records)
                    )
            except Error as e:
                print(f"Select error: {e}")
                return False


# Database instance
database = Database(database_url=config("DATABASE_URL"))
