from uuid import UUID
from core.service import BaseService
from core.database import db_session
from src.users.models import User
from src.users.utils.password_hash import hash_password

from .repository import UserRepository


class UserService(BaseService):
    async def get_user_by_email(self, email: str) -> User:
        async with db_session() as session:
            return await self.repository(session).get_one(email=email)

    async def is_exists(self, email):
        async with db_session() as session:
            return await self.repository(session).exists(email=email)

    async def add(self, data: dict):
        data["password"] = hash_password(data.get("password"))
        return await super().add(data)


user_service = UserService(UserRepository)
