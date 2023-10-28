from uuid import UUID
from pydantic import model_validator, validate_email

from core.exceptions import ValidationError
from core.schemas import Base
from src.auth.schemas import RegisterUser
from src.users.schemas import ReadUser


class ReadPortal(Base):
    id: UUID
    name: str
    phone: str
    email: str
    address: str
    inn: str


class SchoolRegister(Base):
    user: RegisterUser
    portal: ReadPortal

    @model_validator(mode="after")
    def validate_credentials(self):
        if self.portal.phone[0] != "+":
            raise ValueError("Телефон должен начинаться с +")
        if not self.portal.phone[1:].isdigit() or len(self.portal.phone) > 18:
            raise ValueError("Укажите верный номер телефона")
        try:
            validate_email(self.portal.email)
            validate_email(self.user.email)
        except ValidationError as e:
            raise ValueError(str(e))
        return self


class ReadDepartment(Base):
    id: UUID
    name: str


class UserProfile(ReadUser):
    portal: ReadPortal | None
    department: ReadDepartment | None


class UserProfileRead(Base):
    user: UserProfile
