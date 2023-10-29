from datetime import datetime
from uuid import UUID
from core.schemas import Base


class VRUserRead(Base):
    email: str
    role: str
    urlIcon: str | None


class CreateModule(Base):
    name: str


class ModuleRead(CreateModule):
    urlFile: str | None


class SessionRead(Base):
    id: UUID
    date: datetime
    duration: str
    score: int
    maxScore: int
    isSuccessful: bool
    mark: int
    descriptionEvaluationReason: str
    urlRecordingFile: str
