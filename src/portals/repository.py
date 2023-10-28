from core.repository import BaseRepository
from src.portals.models import Portal


class PortalRepository(BaseRepository):
    model = Portal
