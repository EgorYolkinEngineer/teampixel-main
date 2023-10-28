from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from core.exceptions import AlreadyExistError, MultipleRowsFoundError, NoRowsFoundError
from src.auth.service import get_worker_or_403, get_hr_or_403
from src.courses.schemas import CourseRead, CreateCourse
from src.courses.services import course_service
from src.users.models import User


course_router = APIRouter(prefix="/courses", tags=["Course"])


@course_router.get("/user")
async def my_courses(user: User = Depends(get_worker_or_403)) -> list[CourseRead]:
    try:
        return user.department.courses
    except AttributeError:
        raise HTTPException(HTTP_400_BAD_REQUEST, "Сотрудник не привязан ни к одному из отделов")


@course_router.post("/create")
async def create_course(data: CreateCourse, user: User = Depends(get_hr_or_403)) -> CourseRead:
    try:
        return await course_service.create(data.model_dump(), user)
    except AlreadyExistError:
        raise HTTPException(HTTP_400_BAD_REQUEST, "Такого департамента не существует")


@course_router.get("/{pk}")
async def read_course(pk: UUID, user: User = Depends(get_worker_or_403)) -> CourseRead:
    try:
        return await course_service.get_by_department(pk, user.department.name)
    except AttributeError:
        raise HTTPException(HTTP_400_BAD_REQUEST, "Сотрудник не привязан ни к одному из отделов")
    except (MultipleRowsFoundError, NoRowsFoundError):
        raise HTTPException(HTTP_400_BAD_REQUEST, "Сотрудник не соответствует отделу")
