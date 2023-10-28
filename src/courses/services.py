from uuid import UUID

from core.database import db_session
from core.service import BaseService
from src.courses.repositories import CourseRepository, TestRepository
from src.users.models import User


class EducationService(BaseService):
    async def create(self, data: dict[str, str | dict[int, dict[str, str | dict]]] | str, hr: User):
        data["author_id"] = hr.id
        return await super().add(data)

    async def get_by_department(self, pk: UUID, department_name: str):
        async with db_session() as session:
            return await self.repository(session).get_one(id=pk, department_name=department_name)


test_service = EducationService(TestRepository)
course_service = EducationService(CourseRepository)
