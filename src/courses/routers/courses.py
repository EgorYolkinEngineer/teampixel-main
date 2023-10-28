from fastapi import APIRouter, Depends, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from src.auth.service import get_worker_or_403
from src.courses.schemas import CourseRead
from src.users.models import User


course_router = APIRouter(prefix="/courses", tags=["Course"])


@course_router.get("/user")
async def my_courses(user: User = Depends(get_worker_or_403)) -> list[CourseRead]:
    try:
        return user.department.courses
    except AttributeError:
        raise HTTPException(HTTP_400_BAD_REQUEST, "Сотрудник не привязан ни к одному из отделов")
