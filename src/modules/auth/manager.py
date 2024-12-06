from src.shared.auth import authenticate_user, get_password_hash
from src.shared.database import Database, database
from src.shared.error_handler import CustomError
from src.shared.manager import BaseManager


class AuthManager(BaseManager):

    def __init__(self, db: Database = database):
        super().__init__(db)

    async def login(self, user_data):
        user = await authenticate_user(user_data.username, user_data.password)
        if not user:
            raise CustomError("Invalid credentials", 400)

        return await self._with_accessToken(
            user["id"], user["account_type_id"]
        )

    async def register(self, user_data):
        user = await BaseManager.account_exists(email=user_data.email)
        if user:
            raise CustomError("User already exists", 400)

        query = f"""
            INSERT INTO {self.accounts_table}
                (email, password, account_type_id)
            VALUES (%s, %s, %s)
            RETURNING id
        """

        account_id = self.db.commit(
            query,
            (
                user_data.email,
                get_password_hash(user_data.password),
                user_data.account_type_id,
            ),
        )

        return await self._with_accessToken(
            account_id, user_data.account_type_id
        )

    async def get_user(self, user_id):
        query = f"""
            SELECT a.id, a.first_name, a.last_name, a.email, a.phone_number,
                a.state, a.local_government, a.address, a.gender,
                a.account_type_id, at.name AS account_type
            FROM {self.accounts_table} a
            JOIN {self.account_types_table} at ON a.account_type_id = at.id
            WHERE a.id = %s
        """

        user = self.db.select(query, (user_id,))
        if not user:
            raise CustomError("User not found", 404)

        return user
