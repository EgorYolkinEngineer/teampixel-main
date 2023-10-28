from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST

from core.exceptions import AlreadyExistError, MultipleRowsFoundError, NoRowsFoundError
from src.auth.service import get_worker_or_403, get_hr_or_403
from src.courses.schemas import TestContent, CreateTest
from src.users.models import User
from src.courses.services import test_service


test_router = APIRouter(prefix="/tests", tags=["Test"])


@test_router.get("/user")
async def my_tests(user: User = Depends(get_worker_or_403)) -> list[TestContent]:
    try:
        return user.department.tests
    except AttributeError:
        raise HTTPException(HTTP_400_BAD_REQUEST, "Сотрудник не привязан ни к одному из отделов")


@test_router.post("/create")
async def create_test(data: CreateTest, user: User = Depends(get_hr_or_403)) -> TestContent:
    try:
        return await test_service.create(data.model_dump(), user)
    except AlreadyExistError:
        raise HTTPException(HTTP_400_BAD_REQUEST, "Такого департамента не существует или же")


@test_router.get("/{pk}")
async def read_test(pk: UUID, user: User = Depends(get_worker_or_403)) -> TestContent:
    try:
        return await test_service.get_by_department(pk, user.department.name)
    except AttributeError:
        raise HTTPException(HTTP_400_BAD_REQUEST, "Сотрудник не привязан ни к одному из отделов")
    except (MultipleRowsFoundError, NoRowsFoundError):
        raise HTTPException(HTTP_400_BAD_REQUEST, "Сотрудник не соответствует отделу")
