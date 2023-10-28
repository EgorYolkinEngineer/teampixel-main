from core.repository import BaseRepository
from src.courses.models import Course, Test


class TestRepository(BaseRepository):
    model = Test


class CourseRepository(BaseRepository):
    model = Course
