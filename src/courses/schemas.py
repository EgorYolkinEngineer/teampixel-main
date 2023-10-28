from uuid import UUID
from core.schemas import Base


class TestContent(Base):
    id: UUID
    name: str
    department_name: str
    content: dict[int, dict[str, str | dict]]


class CourseRead(Base):
    name: str
    content: str
    department_name: str
