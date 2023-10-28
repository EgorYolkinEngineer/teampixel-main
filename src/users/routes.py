from fastapi import APIRouter, Depends

from src.auth.service import get_user_or_401
from src.users.models import User
from src.portals.schemas import UserProfileRead


user_router = APIRouter(prefix="/users", tags=["User"])


@user_router.get("/me")
async def current_user(user: User = Depends(get_user_or_401)) -> UserProfileRead:
    return UserProfileRead(user=user)
