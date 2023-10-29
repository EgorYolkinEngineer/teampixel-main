from fastapi import HTTPException, Request
from jwt import ExpiredSignatureError
from starlette.status import HTTP_403_FORBIDDEN, HTTP_401_UNAUTHORIZED
from core.exceptions import NoRowsFoundError, TokenException, ValidationError

from src.auth.jwt.token import token_service
from src.auth.schemas import LoginUser, RegisterUser, ResponseLoginUser, ResponseRegisterUser
from src.users.consts import Role
from src.users.models import User
from src.users.service import user_service
from src.users.utils.password_hash import check_password


class Authenticate:
    def __init__(self, raise_exception: bool = True, role: str = None):
        self.raise_exception = raise_exception
        self.role = role

    async def __call__(self, request: Request) -> User | None:
        return await self.is_authenticated(request)

    async def is_authenticated(self, request: Request) -> User | None:
        if not (access_token := request.cookies.get("access_token")):
            if self.raise_exception:
                raise HTTPException(
                    HTTP_401_UNAUTHORIZED, "Unauthorized", headers={"WWW-Authenticate": "Bearer"}
                )
            return None
        try:
            decoded_token = await token_service.decode_token(access_token)
        except ExpiredSignatureError:
            if self.raise_exception:
                raise HTTPException(
                    HTTP_401_UNAUTHORIZED, "Unauthorized", headers={"WWW-Authenticate": "Bearer"}
                )
            return None
        except TokenException:
            if self.raise_exception:
                raise HTTPException(
                    HTTP_401_UNAUTHORIZED, "Unauthorized", headers={"WWW-Authenticate": "Bearer"}
                )
            return None
        if self.role:
            await self._check_role(decoded_token["user_role"])
        try:
            return await user_service.retrieve(pk=decoded_token["user_id"])
        except NoRowsFoundError:
            raise HTTPException(
                HTTP_401_UNAUTHORIZED, "Unauthorized", headers={"WWW-Authenticate": "Bearer"}
            )

    async def _check_role(self, role: str) -> HTTPException | None:
        if role not in (self.role, Role.SUPERUSER.value):
            raise HTTPException(HTTP_403_FORBIDDEN, "Forbidden")


get_user_or_401 = Authenticate()
get_user_or_None = Authenticate(raise_exception=False)
get_superuser_or_403 = Authenticate(role=Role.SUPERUSER.value)
get_superuser_or_None = Authenticate(raise_exception=False, role=Role.SUPERUSER.value)
get_worker_or_403 = Authenticate(role=Role.WORKER.value)
get_admin_or_403 = Authenticate(role=Role.ADMIN.value)
get_hr_or_403 = Authenticate(role=Role.HR.value)
get_hr_or_None = Authenticate(raise_exception=False, role=Role.HR.value)


class AuthService:
    async def login_user(self, model: LoginUser) -> ResponseLoginUser:
        user = await user_service.get_user_by_email(model.email)
        if not check_password(model.password, user.password):
            raise ValidationError("Неверный пароль")
        tokens = await token_service.create_tokens(user)
        return ResponseLoginUser(
            user=user, access_token=tokens.access_token, refresh_token=tokens.refresh_token
        )

    async def register_user(self, model: RegisterUser) -> ResponseRegisterUser:
        user = await user_service.add(model.model_dump())
        tokens = await token_service.create_tokens(user)
        return ResponseRegisterUser(
            user=user, access_token=tokens.access_token, refresh_token=tokens.refresh_token
        )


auth_service = AuthService()
