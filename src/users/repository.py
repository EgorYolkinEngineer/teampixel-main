from core.repository import BaseRepository
from src.users.models import User
from src.users.utils.password_hash import hash_password


class UserRepository(BaseRepository):
    model = User

    async def bulk_create(self, data: list[dict]):
        hash_data = []
        for user in data:
            user["password"] = hash_password(user.get("password"))
            hash_data.append(user)
        return await super().bulk_create(hash_data)
