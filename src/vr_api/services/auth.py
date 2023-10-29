import aiohttp
from aiohttp.client import ContentTypeError

from src.users.models import User
from src.vr_api.services.base import BaseVRService
from src.vr_api.urls import SIGNUP, SINGIN, PROFILE, REFRESH


class VRAuthService(BaseVRService):
    def __init__(self, user: User | None = None, token: str | None = None) -> None:
        self.user = user
        super().__init__(token)

    async def auth(self) -> dict[str, dict | str]:
        credentials = {"email": self.user.email, "password": self.user.password}
        try:
            token_pairs = await self.signup(credentials)
        except ContentTypeError:
            token_pairs = await self.signin(credentials)
        return token_pairs

    async def signup(self, data: dict[str, str]) -> dict[str, dict | str]:
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.post(SIGNUP, json=data) as response:
                return await response.json()

    async def signin(self, data: dict[str, str]):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.post(SINGIN, json=data) as response:
                return await response.json()

    async def profile(self) -> dict[str, str]:
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(PROFILE) as response:
                return await response.json()

    async def refresh(self, token: str) -> dict[str, dict | str]:
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.post(REFRESH, json={"token": token}) as response:
                return await response.json()
