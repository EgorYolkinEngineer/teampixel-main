from src.users.models import User

FIXTURES = {
    User: [
        {
            "id": "12345678-1234-5678-1234-567812345678",
            "first_name": "worker",
            "last_name": "worker",
            "email": "worker",
            "password": "worker",
            "role": "WORKER",
        },
        {
            "id": "22345678-1234-5678-1234-567812345678",
            "first_name": "hr",
            "last_name": "hr",
            "email": "hr",
            "password": "hr",
            "role": "HR",
        },
        {
            "id": "32345678-1234-5678-1234-567812345678",
            "first_name": "admin",
            "last_name": "admin",
            "email": "admin",
            "password": "admin",
            "role": "ADMIN",
        },
        {
            "id": "42345678-1234-5678-1234-567812345678",
            "first_name": "superuser",
            "last_name": "superuser",
            "email": "superuser",
            "password": "superuser",
            "role": "SUPERUSER",
        },
    ],
}
