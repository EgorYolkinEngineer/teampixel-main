import asyncio
from httpx import AsyncClient


async def test_registration(ac: AsyncClient):
    result = await ac.post(
        url="/api/v1/auth/register",
        json={
            "username": "test",
            "password": "test@Test123",
        },
    )
    assert result.status_code == 201
    assert result.cookies.get("access_token")
    assert result.cookies.get("refresh_token")


async def test_login(ac: AsyncClient):
    result = await ac.post(
        url="/api/v1/auth/login",
        json={
            "username": "test",
            "password": "test@Test123",
        },
    )
    assert result.status_code == 200
    assert result.cookies.get("access_token")
    assert result.cookies.get("refresh_token")
