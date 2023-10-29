from fastapi import Depends, Request, HTTPException

from core.config.templates import templates
from core.custom_routers import TemplateRouter
from src.users.consts import Role
from src.users.models import User
from src.auth.service import get_user_or_401

templates_router = TemplateRouter()


def permission_roles(user: User, roles: list[Role]):
    if user.role in roles:
        return True
    else:
        raise HTTPException(
            status_code=403
        )


@templates_router.get("/")
async def possibilities(request: Request):
    return templates.TemplateResponse("possibilities.html", {"request": request})


@templates_router.get("/auth/")
async def auth(request: Request):
    return templates.TemplateResponse("auth.html", {"request": request})


@templates_router.get("/test/{test_id}/")
async def profile_tests(request: Request, test_id: str):
    return templates.TemplateResponse("test.html", {"request": request, 
                                                             "test_id": test_id})
    
    

@templates_router.get("/base/tests/")
async def profile_tests(request: Request, user: User = Depends(get_user_or_401)):
    if permission_roles(user, [Role.HR, Role.ADMIN, Role.SUPERUSER]):
        return templates.TemplateResponse("profile/tests_base.html", {"request": request})


@templates_router.get("/base/tests/check/")
async def profile_tests(request: Request):
    return templates.TemplateResponse("profile/create_test.html", {"request": request})


@templates_router.get("/profile/")
async def profile(request: Request, user: User = Depends(get_user_or_401)):
    if user.role == Role.WORKER:
        return templates.TemplateResponse("profile/worker.html", {"request": request, 
                                                                  "role": user.role.value})
    elif user.role == Role.HR:
        return templates.TemplateResponse("profile/hr.html", {"request": request, 
                                                              "role": user.role.value})
    elif user.role == Role.ADMIN:
        return templates.TemplateResponse("profile/admin.html", {"request": request, 
                                                                "role": user.role.value})


@templates_router.get("/profile/tests/")
async def profile_tests(request: Request):
    return templates.TemplateResponse("profile/tests.html", {"request": request})


@templates_router.get("/profile/results/")
async def profile_results(request: Request):
    return templates.TemplateResponse("profile/tests.html", {"request": request})


@templates_router.get("/profile/education/")
async def profile_education(request: Request):
    return templates.TemplateResponse("profile/education.html", {"request": request})


@templates_router.get("/school/create/")
async def auth(request: Request):
    return templates.TemplateResponse("register_admin.html", {"request": request})


@templates_router.get("/company/")
async def auth(request: Request):
    return templates.TemplateResponse("company.html", {"request": request})


@templates_router.get("/course/{course_id}/")
async def profile_tests(request: Request, course_id: str):
    return templates.TemplateResponse("profile/course.html", {"request": request, 
                                                             "course_id": course_id})
    
    