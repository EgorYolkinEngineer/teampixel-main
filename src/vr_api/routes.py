from fastapi import APIRouter, Depends, HTTPException, Request, Response
from starlette.status import HTTP_400_BAD_REQUEST

from src.auth.service import get_user_or_401
from src.users.models import User
from src.vr_api.auth import VRAuthService
from src.vr_api.schemas import VRUserRead

vr_router = APIRouter(prefix="/vr", tags=["VR"])


@vr_router.post("/auth")
async def authenticate(user: User = Depends(get_user_or_401)) -> Response:
    auth = await VRAuthService(user).auth()
    if not (tokens := auth.get("tokenPair")):
        raise HTTPException(HTTP_400_BAD_REQUEST, "Не верные данные")
    response = Response()
    response.set_cookie("vr_access_token", tokens["accessToken"])
    response.set_cookie("vr_refresh_token", tokens["refreshToken"])
    return response


@vr_router.get("/profile")
async def vr_worker_profile(request: Request) -> VRUserRead:
    if not (vr_access_token := request.cookies.get("vr_access_token")):
        raise HTTPException(HTTP_400_BAD_REQUEST, "Пользователь не авторизован в системе VR")
    return await VRAuthService().profile(vr_access_token)
