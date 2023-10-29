import aiohttp
from src.vr_api.services.base import BaseVRService
from src.vr_api.urls import ONE_MODULE, CREATE_MODULE, ALL_MODULES


class ModuleService(BaseVRService):
    async def all(self):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(ALL_MODULES) as response:
                return await response.json()

    async def create(self, data: dict[str, str]):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.post(CREATE_MODULE, json=data) as response:
                return await response.json()

    async def get(self, name):
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(ONE_MODULE + name) as response:
                return await response.json()
