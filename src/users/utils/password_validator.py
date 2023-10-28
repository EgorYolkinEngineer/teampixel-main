import sys
from abc import ABC, abstractmethod
from typing import Type, TypeVar

from core.exceptions import ValidationError
from src.users import PASSWORD_VALIDATORS


class AbstractValidator(ABC):
    @abstractmethod
    def validate(self, password: str):
        pass


Validator = TypeVar("Validator", bound=AbstractValidator)


def validate_password(password):
    for validator in PASSWORD_VALIDATORS:
        validator_class: Type[Validator] = getattr(sys.modules[__name__], validator)
        validator_class().validate(password)


class MinimumLengthValidator(AbstractValidator):
    def __init__(self, min_length=6):
        self.min_length = min_length

    def validate(self, password: str):
        if len(password) < self.min_length:
            raise ValidationError(f"Пароль должен содержать не менее {self.min_length} символов.")


class NumericPasswordValidator(AbstractValidator):
    def validate(self, password: str):
        if password.isdigit():
            raise ValidationError("Пароль не должен содержать только цифры")


class DifferentCaseValidator(AbstractValidator):
    def validate(self, password: str):
        is_upper = any(char.isupper() for char in password)
        is_lower = any(char.islower() for char in password)
        if not (is_lower and is_upper):
            raise ValidationError("Пароль должен содержать сиволы в верхнем и нижнем регистре")


class SymbolSValidator(AbstractValidator):
    def validate(self, password: str):
        if password.isalnum() or password.isalpha():
            raise ValidationError(
                "Пароль должен содержать как минимум один специальный символ и одну цифру"
            )
