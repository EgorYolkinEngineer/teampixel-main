from core.schemas import Base


class TestContent(Base):
    name: str
    department_name: str
    content: dict[int, dict[str, str | dict]]
