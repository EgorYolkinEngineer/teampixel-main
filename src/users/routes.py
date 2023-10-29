from uuid import UUID

from fastapi import APIRouter, Depends, File, HTTPException, UploadFile
from starlette.status import HTTP_400_BAD_REQUEST

from core.exceptions import NoRowsFoundError
from core.service import generic_service
from core.config.templates import MEDIA_DIR
from src.auth.service import get_user_or_401
from src.portals.schemas import UserProfileRead
from src.users.schemas import TextReview, UpdateUser
from src.users.models import Review, User
from src.users.service import user_service


user_router = APIRouter(prefix="/users", tags=["User"])


@user_router.get("/me")
async def current_user(user: User = Depends(get_user_or_401)) -> UserProfileRead:
    return UserProfileRead(user=user)


@user_router.patch("/update")
async def update_profile(data: UpdateUser, user: User = Depends(get_user_or_401)) -> UpdateUser:
    user = await user_service.update(user.id, data.model_dump(exclude_unset=True))
    return UpdateUser(
        first_name=user.first_name, last_name=user.last_name, patronymic=user.patronymic
    )


@user_router.get("/reviews")
async def reviews_list() -> list[TextReview]:
    service = await generic_service(Review)
    return await service.all()


@user_router.post("/reviews/create", dependencies=[Depends(get_user_or_401)])
async def add_review(data: TextReview) -> TextReview:
    service = await generic_service(Review)
    return await service.add(data.model_dump())


@user_router.delete("/dismiss/{worker_id}")
async def dismissal(worker_id: UUID) -> UpdateUser:
    try:
        return await user_service.update(worker_id, {"department_id": None})
    except NoRowsFoundError:
        raise HTTPException(HTTP_400_BAD_REQUEST, "Такого департамента не существует")


@user_router.put("/update/avatar")
async def upload_files(image: UploadFile = File(), user: User = Depends(get_user_or_401)):
    file_extension = image.filename.split(".")[-1]
    file_location = f"{MEDIA_DIR}/{user.id}.{file_extension}"

    with open(file_location, "wb+") as file_object:
        file_object.write(image.file.read())

    return {"image": image, "path": file_location}
