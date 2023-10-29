from uuid import UUID
import aiohttp
from src.vr_api.services.base import BaseVRService
from src.vr_api.urls import ALL_SESSIONS, ONE_SESSION


class SessionService(BaseVRService):
    async def all(self, module_name):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(ALL_SESSIONS + module_name) as response:
                return await response.json()

    async def get(self, pk: UUID):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(ONE_SESSION + str(pk)) as response:
                return await response.json()
