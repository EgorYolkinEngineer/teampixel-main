from core.service import BaseService
from src.courses.repositories import CourseRepository, TestRepository
from src.users.models import User


class TestService(BaseService):
    async def create(self, data: dict[str, str | dict[int, dict[str, str | dict]]], hr: User):
        data["author_id"] = hr.id
        return await super().add(data)


class CourseService(BaseService):
    pass


test_service = TestService(TestRepository)
course_service = CourseService(CourseRepository)
