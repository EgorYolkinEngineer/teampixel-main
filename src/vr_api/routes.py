from fastapi import APIRouter, Depends

from src.auth.service import get_user_or_401
from src.users.models import User
from src.vr_api.auth import VRAuthService

vr_router = APIRouter(prefix="/vr", tags=["VR"])


@vr_router.post("/auth")
async def authenticate(user: User = Depends(get_user_or_401)):
    vr_auth_service = VRAuthService(user)
    tokens = await vr_auth_service.auth()["tokenPair"]
    # try:
    #     return await vr_auth_service.profile(access=tokens)
