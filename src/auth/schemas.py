from pydantic import model_validator
from core.exceptions import ValidationError

from core.schemas import Base, validate_email
from src.users.schemas import ReadUser
from src.users.utils.password_validator import validate_password


class LoginUser(Base):
    email: str
    password: str


class RegisterUser(LoginUser):
    first_name: str
    last_name: str

    @model_validator(mode="after")
    def validate_credentials(self):
        try:
            validate_password(self.password)
        except ValidationError as e:
            raise ValueError(str(e))
        try:
            validate_email(self.email)
        except ValidationError as e:
            raise ValueError(str(e))

        return self


class RefreshToken(Base):
    refresh_token: str


class Tokens(RefreshToken):
    access_token: str


class ResponseRegisterUser(Tokens):
    user: ReadUser


class ResponseLoginUser(Tokens):
    user: ReadUser
