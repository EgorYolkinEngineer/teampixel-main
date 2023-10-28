from fastapi import APIRouter, Depends

from src.auth.service import get_worker_or_403
from src.courses.schemas import CourseRead
from src.users.models import User


course_router = APIRouter(prefix="/courses", tags=["Course"])


@course_router.get("/user")
async def my_courses(user: User = Depends(get_worker_or_403)) -> list[CourseRead]:
    return user.courses
