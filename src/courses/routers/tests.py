from fastapi import APIRouter, Depends

from core.service import generic_service
from src.auth.service import get_worker_or_403
from src.courses.models import Test
from src.users.models import User


test_router = APIRouter(prefix="/tests", tags=["Test"])


@test_router.get("/all")
async def test_list():
    service = await generic_service(Test)
    return await service.all()


@test_router.get("/user")
async def my_tests(user: User = Depends(get_worker_or_403)):
    return await user.tests
