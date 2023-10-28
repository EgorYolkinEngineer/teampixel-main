from fastapi import APIRouter

from .courses import course_router
from .tests import test_router

education_router = APIRouter()
education_router.include_router(course_router)
education_router.include_router(test_router)
