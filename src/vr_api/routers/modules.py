from fastapi import APIRouter, Depends

from src.vr_api.services import get_access_token
from src.vr_api.services.module import ModuleService

module_router = APIRouter(prefix="/modules")


@module_router.get("/all")
async def modules_list(token: str = Depends(get_access_token)):
    pass


@module_router.get("/{module_name}")
async def get_module(module_name: str):
    pass


@module_router.post("/create")
async def create_module():
    pass
