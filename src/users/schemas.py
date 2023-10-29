from datetime import datetime
from uuid import UUID
from core.schemas import Base
from src.users.consts import Role


class ResponseReadUser(Base):
    email: str
    first_name: str
    last_name: str
    patronymic: str | None
    birth_date: datetime | None
    role: Role


class ReadUser(ResponseReadUser):
    id: UUID


class UpdateUser(Base):
    first_name: str
    last_name: str
    patronymic: str | None = None


class TextReview(Base):
    text: str
