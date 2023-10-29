from datetime import datetime, timedelta

from jwt import ExpiredSignatureError, PyJWTError, decode, encode

from core.config.jwt import config_token
from core.config.settings import settings
from core.exceptions import TokenException
from src.auth.jwt.base import AbstractToken
from src.auth.schemas import Tokens
from src.users.models import User
from src.users.service import user_service


class TokenService(AbstractToken):
    secret_key = settings.SECRET_KEY
    algorithm = config_token.ALGORITHM
    access_token_lifetime = config_token.ACCESS_TOKEN_LIFETIME
    refresh_token_lifetime = config_token.REFRESH_TOKEN_LIFETIME
    refresh_token_rotate_min_lifetime = config_token.REFRESH_TOKEN_ROTATE_MIN_LIFETIME

    async def create_tokens(self, user: User) -> Tokens:
        access_token = await self.generate_access_token(user)
        refresh_token = await self.generate_refresh_token(user)
        return Tokens(access_token=access_token, refresh_token=refresh_token)

    async def generate_access_token(self, user: User) -> str:
        expire = datetime.utcnow() + timedelta(minutes=self.access_token_lifetime)
        payload = {
            "token_type": "access",
            "user_id": str(user.id),
            "user_role": user.role.value,
            "exp": expire,
        }
        return await self.encode_token(payload)

    async def generate_refresh_token(self, user: User) -> str:
        expire = datetime.utcnow() + timedelta(seconds=self.refresh_token_lifetime)
        payload = {
            "token_type": "refresh",
            "user_id": str(user.id),
            "user_role": user.role.value,
            "exp": expire,
        }
        return await self.encode_token(payload)

    async def refresh(self, refresh_token: str) -> Tokens:
        decoded_refresh = await self.decode_token(refresh_token)
        if decoded_refresh["token_type"] != "refresh":
            raise TokenException("Not a refresh token")
        return await self.create_tokens(await user_service.retrieve(decoded_refresh["user_id"]))

    async def encode_token(self, payload: dict) -> str:
        return encode(payload, self.secret_key, self.algorithm)

    async def decode_token(self, token: str) -> dict:
        try:
            return decode(token, self.secret_key, self.algorithm)  # type: ignore
        except ExpiredSignatureError:
            raise ExpiredSignatureError("Token lifetime is expired")
        except PyJWTError:
            raise TokenException("Token is invalid")


token_service = TokenService()
