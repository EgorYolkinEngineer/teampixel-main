from abc import ABC, abstractmethod


class AbstractToken(ABC):
    """JWT abstract model."""

    secret_key = None
    algorithm = None
    access_token_lifetime = None

    @abstractmethod
    async def generate_access_token(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def generate_refresh_token(self, data: dict):
        raise NotImplementedError

    @abstractmethod
    async def encode_token(self, payload: dict):
        raise NotImplementedError

    @abstractmethod
    async def decode_token(self, token: str):
        raise NotImplementedError
