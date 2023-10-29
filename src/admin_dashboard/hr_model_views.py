from sqladmin import ModelView
from src.portals.models import Company, Department, Portal
from src.courses.models import Course, Test
from src.users.models import User, Review


class UserHR(ModelView, model=User):
    """User model in admin dashboard."""

    column_list = [User.id, User.first_name, User.last_name, User.patronymic, User.created_at]
    can_create = True
    can_edit = True
    can_delete = False
    can_view_details = True


class TestHR(ModelView, model=Test):
    """User model in admin dashboard."""

    column_list = [Test.id, Test.name, Test.content, Test.department_name]
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True


class CourseHR(ModelView, model=Course):
    """User model in admin dashboard."""

    column_list = [Course.id, Course.name, Course.content, Course.department_name]
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True


class DepartmentHR(ModelView, model=Department):
    """User model in admin dashboard."""

    column_list = [Department.id, Department.name]
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
