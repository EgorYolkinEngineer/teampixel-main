from core.service import BaseService
from src.auth.schemas import ResponseRegisterUser, RegisterUser
from src.auth.service import auth_service
from src.portals.repository import PortalRepository
from src.users.consts import Role


class PortalService(BaseService):
    async def register_school(self, data: dict[str, dict[str, str]]) -> ResponseRegisterUser:
        data["user"]["role"] = Role.ADMIN.value
        response = await auth_service.register_user(RegisterUser(**data["user"]))
        data["portal"]["admin_id"] = response.user.id
        await super().add(data["portal"])
        return response


portal_service = PortalService(PortalRepository)
