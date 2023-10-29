from fastapi import HTTPException, Request
from starlette.status import HTTP_400_BAD_REQUEST


async def get_access_token(request: Request) -> str:
    if not (token := request.cookies.get("vr_access_token")):
        raise HTTPException(HTTP_400_BAD_REQUEST, "Пользователь не авторизован в системе VR")
    return token


async def get_refresh_token(request: Request) -> str:
    if not (token := request.cookies.get("vr_refresh_token")):
        raise HTTPException(HTTP_400_BAD_REQUEST, "Пользователь не авторизован в системе VR")
    return token
