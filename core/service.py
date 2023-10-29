from core.database import db_session
from core.repository import BaseRepository


class BaseService:
    def __init__(self, repository: type[BaseRepository]) -> None:
        self.repository = repository

    async def add(self, data: dict = None):
        async with db_session() as session:
            result = await self.repository(session).create(data)
            await session.commit()
            return result

    async def bulk_add(self, data: list[dict]):
        async with db_session() as session:
            result = await self.repository(session).bulk_create(data)
            await session.commit()
            return result

    async def all(self):
        async with db_session() as session:
            return await self.repository(session).all()

    async def retrieve(self, pk):
        async with db_session() as session:
            return await self.repository(session).get_one(id=pk)

    async def update(self, pk, data: dict = None):
        async with db_session() as session:
            result = await self.repository(session).update(data, {"id": pk})
            await session.commit()
            return result

    async def filters(self, filters: dict[str, str]):
        async with db_session() as session:
            return await self.repository(session).filter(filters)

    async def delete(self, pk):
        async with db_session() as session:
            await self.repository(session).delete(id=pk)
            await session.commit()


async def generic_service(_model, service=BaseService, repository=BaseRepository):
    class Repository(repository):
        model = _model

    return service(Repository)
