import sys
from getpass import getpass

from core.commands import func_registry
from core.exceptions import ValidationError
from src.users.service import user_service
from src.users.utils.password_hash import hash_password
from src.users.utils.password_validator import validate_password


@func_registry(description="Create new superuser in DB")
async def createsuperuser():
    user_data = {
        "email": await get_email(),
        **get_full_name(),
        "password": get_password(),
        "role": "SUPERUSER",
    }
    await user_service.add(user_data)
    sys.stdout.write("Superuser successfully created.")


async def get_email() -> str:
    while True:
        email = input("Please provide your email: ")
        if not email:
            sys.stdout.write("Your email could not be blank line\n")
        elif await user_service.is_exists(email):
            sys.stdout.write("Email already exists\n")
        else:
            break
    return email


def get_full_name() -> dict[str, str]:
    full_name = {}
    for name in ("first_name", "last_name"):
        while True:
            input_name = input(f"Please provide your {name}: ")
            if not input_name:
                sys.stdout.write(f"Your {name} could not be blank line\n")
            else:
                full_name[name] = input_name
                break
    return full_name


def get_password() -> str | bytes:
    while True:
        password = getpass()
        if not password:
            sys.stdout.write("Password can't be blank line\n")
            continue

        password_again = getpass(prompt="Password again: ")

        if password != password_again:
            sys.stdout.write("Password doesn't match\n")
            continue

        try:
            validate_password(password)
        except ValidationError as error:
            sys.stdout.write(f"\033[91m\n{str(error)}\n\033[0m")
            is_it_ok = input(
                "Are you sure you want to use this password? Press 'Y/y' for confirmation: "
            )
            if is_it_ok.lower() == "y":
                return hash_password(password)
        else:
            break
    return password
