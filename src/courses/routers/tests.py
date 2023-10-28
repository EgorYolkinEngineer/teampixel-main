from fastapi import APIRouter, Depends, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST
from core.exceptions import AlreadyExistError
from core.service import generic_service
from src.auth.service import get_worker_or_403, get_hr_or_403
from src.courses.models import Test
from src.courses.schemas import TestContent
from src.users.models import User
from src.courses.services import test_service


test_router = APIRouter(prefix="/tests", tags=["Test"])


@test_router.get("/all")
async def test_list():
    service = await generic_service(Test)
    return await service.all()


@test_router.get("/user")
async def my_tests(user: User = Depends(get_worker_or_403)):
    return await user.tests


@test_router.post("/create")
async def create_test(data: TestContent, user: User = Depends(get_hr_or_403)) -> TestContent:
    try:
        return await test_service.create(data.model_dump(), user)
    except AlreadyExistError:
        raise HTTPException(HTTP_400_BAD_REQUEST, "Такого департамента не существует")
