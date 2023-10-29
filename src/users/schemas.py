from datetime import datetime
from uuid import UUID
from core.schemas import Base
from src.users.consts import Role


class ReadUser(Base):
    id: UUID
    email: str
    first_name: str
    last_name: str
    patronymic: str | None
    birth_date: datetime | None
    role: Role


class UpdateUser(Base):
    first_name: str
    last_name: str
    patronymic: str | None = None
