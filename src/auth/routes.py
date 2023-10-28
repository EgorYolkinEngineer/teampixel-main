from fastapi import HTTPException
from fastapi.routing import APIRouter
from starlette.status import HTTP_400_BAD_REQUEST

from core.exceptions import AlreadyExistError, NoRowsFoundError, ValidationError
from src.auth.schemas import LoginUser, RegisterUser, ResponseLoginUser, ResponseRegisterUser
from src.auth.service import auth_service


auth_router = APIRouter(prefix="/auth", tags=["Auth"])


@auth_router.post("/register", status_code=201)
async def register(data: RegisterUser) -> ResponseRegisterUser:
    try:
        return await auth_service.register_user(data)
    except AlreadyExistError:
        raise HTTPException(HTTP_400_BAD_REQUEST, "Пользователь с такими данными уже существует")


@auth_router.post("/login")
async def login(data: LoginUser) -> ResponseLoginUser:
    try:
        return await auth_service.login_user(data)
    except ValidationError as e:
        raise HTTPException(HTTP_400_BAD_REQUEST, str(e))
    except NoRowsFoundError:
        raise HTTPException(HTTP_400_BAD_REQUEST, "Неверный email")
