from src.users.models import User
from src.courses.models import Course, Test
from src.portals.models import Portal, Department

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
    Portal: [
        {
            "id": "12345678-1234-5678-1234-567812345678",
            "name": "portal1",
            "address": "portal1",
            "phone": "+7999999999",
            "email": "portal1",
            "inn": "111222",
            "admin_id": "32345678-1234-5678-1234-567812345678",
        },
        {
            "id": "22345678-1234-5678-1234-567812345678",
            "name": "portal2",
            "address": "portal2",
            "phone": "+790000000000",
            "email": "portal2",
            "inn": "121212",
            "admin_id": "32345678-1234-5678-1234-567812345678",
        },
    ],
    Department: [
        {
            "id": "12345678-1234-5678-1234-567812345678",
            "name": "department1",
            "portal_id": "12345678-1234-5678-1234-567812345678",
        },
        {
            "id": "22345678-1234-5678-1234-567812345678",
            "name": "department2",
            "portal_id": "22345678-1234-5678-1234-567812345678",
        },
    ],
    Test: [
        {
            "id": "12345678-1234-5678-1234-567812345678",
            "name": "test1",
            "department_name": "department1",
            "author_id": "22345678-1234-5678-1234-567812345678",
            "content": {
                "1": {
                    "question1": "string",
                    "question2": "string",
                },
                "2": {
                    "question1": "string",
                    "question2": "string",
                },
            },
        },
        {
            "id": "22345678-1234-5678-1234-567812345678",
            "name": "test2",
            "department_name": "department2",
            "author_id": "22345678-1234-5678-1234-567812345678",
            "content": {
                "1": {
                    "question1": "string",
                    "question2": "string",
                },
                "2": {
                    "question1": "string",
                    "question2": "string",
                },
            },
        },
    ],
    Course: [
        {
            "id": "12345678-1234-5678-1234-567812345678",
            "name": "course1",
            "department_name": "department1",
            "author_id": "22345678-1234-5678-1234-567812345678",
            "content": "text course1",
        },
        {
            "id": "22345678-1234-5678-1234-567812345678",
            "name": "course1",
            "department_name": "department2",
            "author_id": "22345678-1234-5678-1234-567812345678",
            "content": "text course1",
        },
    ],
}
