from fastapi import APIRouter

from src.templates.routes import templates_router
from src.auth.routes import auth_router
from src.courses.routers import education_router
from src.portals.routes import portal_router, department_router
from src.users.routes import user_router


def get_api_router() -> APIRouter:
    router = APIRouter(prefix="/api/v1")
    router.include_router(auth_router)
    router.include_router(education_router)
    router.include_router(portal_router)
    router.include_router(department_router)
    router.include_router(user_router)
    return router


def get_template_router() -> APIRouter:
    router = APIRouter()
    router.include_router(templates_router)
    return router
