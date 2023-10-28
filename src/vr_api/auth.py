import aiohttp
from aiohtp.client import ContentTypeError

from src.users.models import User
from src.vr_api.urls import SIGNUP, SINGIN, PROFILE, REFRESH


class VRAuthService:
    header: str = {"ngrok-skip-browser-warning": "69420"}

    async def auth(self, user: User):
        credentials = {"email": user.email, "password": user.password}
        try:
            token_pairs = await self.signup(credentials)
        except ContentTypeError:
            token_pairs = await self.signin(credentials)
        return token_pairs

    async def signup(self, data: dict[str, str]):
        async with aiohttp.ClientSession() as session:
            async with session.post(SIGNUP, json=data) as response:
                return await response.json()

    async def signin(self, data: dict[str, str]):
        async with aiohttp.ClientSession(headers=self.header) as session:
            async with session.post(SINGIN, json=data) as response:
                return await response.json()


vr_auth_service = VRAuthService()
