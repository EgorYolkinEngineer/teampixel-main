from fastapi import APIRouter

from src.vr_api.routers.auth import auth_router
from src.vr_api.routers.modules import module_router
from src.vr_api.routers.session import session_router


vr_router = APIRouter(prefix="/vr", tags=["VR"])
vr_router.include_router(auth_router)
vr_router.include_router(module_router)
vr_router.include_router(session_router)
