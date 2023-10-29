from pydantic import Field
from core.schemas import Base


class VRUserRead(Base):
    email: str
    role: str
    url_icon: str | None = Field(alias="urlIcon")
