from fastapi import APIRouter, Depends, HTTPException
from starlette.status import HTTP_400_BAD_REQUEST
from src.auth.schemas import VRTokens

from src.auth.service import get_user_or_401
from src.users.models import User
from src.vr_api.auth import VRAuthService

vr_router = APIRouter(prefix="/vr", tags=["VR"])


@vr_router.post("/auth")
async def authenticate(user: User = Depends(get_user_or_401)):
    vr_auth_service = VRAuthService(user)
    result = await vr_auth_service.auth()
    tokens = result.get("tokenPair")
    if not tokens:
        raise HTTPException(HTTP_400_BAD_REQUEST, "Не верные данные")
    return VRTokens(vr_access_token=tokens["accessToken"], vr_refresh_token=tokens["refreshToken"])
    # try:
    #     return await vr_auth_service.profile(access=tokens)
