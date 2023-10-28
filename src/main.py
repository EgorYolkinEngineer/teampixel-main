from fastapi.concurrency import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI
from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from redis import asyncio as aioredis

from core.config.templates import templates
from core.database import base_db_session
from core.config.settings import settings
from core.config.templates import STATIC_DIR, STATIC_PATH, MEDIA_DIR, MEDIA_PATH
from core.config.redis import config_redis

from src.admin_dashboard.admin import CustomAdmin
from src.routers import get_api_router, get_template_router
from src.admin_dashboard import models_views
from src.admin_dashboard.auth_backend import AdminAuthenticationBackend


@asynccontextmanager
async def lifespan(app: FastAPI):
    redis = aioredis.from_url(config_redis.redis_url)
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield


def http_exception_handler(request: Request, exc: HTTPException):
    print(exc.detail)
    return templates.TemplateResponse(f"errors/{exc.status_code}.html", {"request": request})


def http_404_exception_handler(request: Request, exc: HTTPException):
    return templates.TemplateResponse(f"errors/{exc.status_code}.html", {"request": request})


exception_handlers = {
    404: http_404_exception_handler,
    401: http_exception_handler,
    403: http_exception_handler,
    404: http_exception_handler,
    500: http_exception_handler,
}

# Main app
app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
    version=settings.VERSION,
    lifespan=lifespan,
    exception_handlers=exception_handlers,
)


# Admin settings
admin_auth_backend = AdminAuthenticationBackend(
    settings.SECRET_KEY,
)
admin = CustomAdmin(
    app,
    base_db_session.engine,
    base_url="/dashboard/admin",
    title="⚙️ #TeamPixel dashboard",
    authentication_backend=admin_auth_backend,
)


admin.add_view(models_views.UserAdmin)
admin.add_view(models_views.DepartmentAdmin)
admin.add_view(models_views.PortalAdmin)
admin.add_view(models_views.TestAdmin)
admin.add_view(models_views.CourseAdmin)


# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Static && Media files
app.mount(STATIC_PATH, StaticFiles(directory=STATIC_DIR), name="static")
app.mount(MEDIA_PATH, StaticFiles(directory=MEDIA_DIR), name="media")

# Include other routers
app.include_router(get_api_router())
app.include_router(get_template_router())
