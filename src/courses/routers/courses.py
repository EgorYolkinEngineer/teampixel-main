from fastapi import APIRouter, Depends

from core.service import generic_service
from src.auth.service import get_worker_or_403
from src.courses.models import Course
from src.users.models import User


course_router = APIRouter(prefix="/courses", tags=["Course"])


@course_router.get("/all")
async def course_list():
    service = await generic_service(Course)
    return await service.all()


@course_router.get("/user")
async def my_courses(user: User = Depends(get_worker_or_403)):
    return await user.courses
