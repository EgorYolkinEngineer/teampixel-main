from sqladmin import ModelView
from src.portals.models import Company, Department, Portal
from src.courses.models import Course, Test
from src.users.models import User


class UserAdmin(ModelView, model=User):
    """User model in admin dashboard."""

    column_list = [User.id, User.first_name, User.last_name, User.created_at]
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True


class TestAdmin(ModelView, model=Test):
    """User model in admin dashboard."""

    column_list = [Test.id, Test.name, Test.content, Test.department_name]
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True


class CourseAdmin(ModelView, model=Course):
    """User model in admin dashboard."""

    column_list = [Course.id, Course.name, Course.content, Course.department_name]
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True


class PortalAdmin(ModelView, model=Portal):
    """User model in admin dashboard."""

    column_list = [
        Portal.id,
        Portal.name,
        Portal.address,
        Portal.phone,
        Portal.email,
        Portal.main_hex_color,
    ]
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True


class CompanyAdmin(ModelView, model=Company):
    """User model in admin dashboard."""

    column_list = [Company.id, Company.name]
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True


class DepartmentAdmin(ModelView, model=Department):
    """User model in admin dashboard."""

    column_list = [Department.id, Department.name]
    can_create = True
    can_edit = True
    can_delete = True
    can_view_details = True
