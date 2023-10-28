from uuid import UUID
from core.schemas import Base


class CreateTest(Base):
    name: str
    department_name: str
    content: dict[int, dict[str, str | dict]]


class TestContent(CreateTest):
    id: UUID


class CreateCourse(Base):
    name: str
    content: str
    department_name: str


class CourseRead(CreateCourse):
    id: UUID
