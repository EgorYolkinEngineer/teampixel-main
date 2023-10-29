from aiohttp import ContentTypeError
from fastapi import APIRouter, Depends, HTTPException
from starlette.status import HTTP_404_NOT_FOUND

from src.vr_api.services import get_access_token
from src.vr_api.services.module import ModuleService
from src.vr_api.schemas import CreateModule, ModuleRead

module_router = APIRouter(prefix="/modules")


@module_router.get("/all")
async def modules_list(token: str = Depends(get_access_token)) -> list[ModuleRead]:
    return await ModuleService(token=token).all()


@module_router.get("/{module_name}")
async def get_module(module_name: str, token: str = Depends(get_access_token)) -> ModuleRead:
    try:
        return await ModuleService(token=token).get(module_name)
    except ContentTypeError:
        raise HTTPException(HTTP_404_NOT_FOUND, "Not found")
