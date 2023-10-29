from uuid import UUID
from aiohttp import ContentTypeError
from fastapi import APIRouter, Depends, HTTPException
from starlette.status import HTTP_404_NOT_FOUND

from src.vr_api.services import get_access_token
from src.vr_api.schemas import SessionRead
from src.vr_api.services.session import SessionService

session_router = APIRouter(prefix="/sessions")


@session_router.get("/all/{module_name}")
async def modules_list(
    module_name: str, token: str = Depends(get_access_token)
) -> list[SessionRead]:
    try:
        return await SessionService(token=token).all(module_name)
    except ContentTypeError:
        raise HTTPException(HTTP_404_NOT_FOUND, "Not found")


@session_router.get("/{pk}")
async def get_module(pk: UUID, token: str = Depends(get_access_token)) -> SessionRead:
    try:
        return await SessionService(token=token).get(pk)
    except ContentTypeError:
        raise HTTPException(HTTP_404_NOT_FOUND, "Not found")
