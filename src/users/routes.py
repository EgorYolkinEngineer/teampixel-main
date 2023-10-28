from fastapi import APIRouter, Depends

from src.auth.service import get_user_or_401
from src.portals.schemas import UserProfileRead
from src.users.schemas import UpdateUser
from src.users.models import User
from src.users.service import user_service


user_router = APIRouter(prefix="/users", tags=["User"])


@user_router.get("/me")
async def current_user(user: User = Depends(get_user_or_401)) -> UserProfileRead:
    return UserProfileRead(user=user)


@user_router.patch("/update")
async def update_profile(data: UpdateUser, user: User = Depends(get_user_or_401)) -> UpdateUser:
    user = await user_service.update(user.id, data.model_dump())
    return UpdateUser(
        first_name=user.first_name, last_name=user.last_name, patronymic=user.patronymic
    )
