from fastapi import APIRouter, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST
from core.exceptions import AlreadyExistError

from src.auth.schemas import ResponseRegisterUser
from src.portals.schemas import SchoolRegister
from src.portals.service import portal_service


portal_router = APIRouter(prefix="/school/register", tags=["Portal"])


@portal_router.post("/")
async def create_school(data: SchoolRegister) -> ResponseRegisterUser:
    try:
        return await portal_service.register_school(data.model_dump())
    except AlreadyExistError:
        raise HTTPException(
            HTTP_400_BAD_REQUEST, "Школа или пользователь с такими данными уже существует"
        )
