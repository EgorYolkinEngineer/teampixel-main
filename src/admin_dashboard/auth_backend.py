from sqladmin.authentication import AuthenticationBackend
from starlette.requests import Request

from src.auth.service import auth_service, get_superuser_or_None
from src.auth.service import get_hr_or_None
from src.auth.schemas import LoginUser, Tokens
from src.users.models import User


class AdminAuthenticationBackend(AuthenticationBackend):
    """Admin dashboard auth. backend."""

    async def login(self, request: Request) -> Tokens:
        form = await request.form()
        email, password = form["email"], str(form["password"])
        model = LoginUser(email=email, password=password)
        return await auth_service.login_user(model)

    async def authenticate(self, request: Request) -> User | None:
        return await get_superuser_or_None(request)


class HrAuthenticationBackend(AuthenticationBackend):
    """HR dashboard auth. backend."""

    async def login(self, request: Request) -> Tokens:
        form = await request.form()
        email, password = form["email"], str(form["password"])
        model = LoginUser(email=email, password=password)
        return await auth_service.login_user(model)

    async def authenticate(self, request: Request) -> User | None:
        return await get_hr_or_None(request)
