from pydantic import BaseModel

from core.exceptions import ValidationError


class Base(BaseModel):
    class Config:
        from_attributes = True


def validate_email(email: str):
    if "@" not in email or "." not in email:
        raise ValidationError("Не верно указан адрес электонной почты")
