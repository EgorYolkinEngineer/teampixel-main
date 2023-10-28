from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST
from core.exceptions import AlreadyExistError
from core.service import generic_service

from src.auth.schemas import ResponseRegisterUser
from src.portals.models import Department
from src.portals.schemas import ReadDepartment, SchoolRegister
from src.portals.service import portal_service


portal_router = APIRouter(prefix="/school", tags=["Portal"])
department_router = APIRouter(prefix="/departments", tags=["Portal"])


@portal_router.post("/register")
async def create_school(data: SchoolRegister) -> ResponseRegisterUser:
    try:
        return await portal_service.register_school(data.model_dump())
    except AlreadyExistError:
        raise HTTPException(
            HTTP_400_BAD_REQUEST, "Школа или пользователь с такими данными уже существует"
        )


@department_router.get("/all")
async def departments_list() -> list[ReadDepartment]:
    service = await generic_service(Department)
    return await service.all()
