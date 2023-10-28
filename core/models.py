import datetime
import os
import re
import sys
import uuid

from sqlalchemy import TIMESTAMP
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import DeclarativeBase, Mapped, declared_attr, mapped_column


class Base(DeclarativeBase):
    """Base SQLAlchemy model."""

    id: Mapped[uuid.UUID] = mapped_column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)

    type_annotation_map = {
        datetime.datetime: TIMESTAMP(timezone=True),
    }

    @declared_attr
    def __tablename__(cls):
        """Autocreate tables name."""

        class_file_path = os.path.abspath(sys.modules[cls.__module__].__file__)  # type: ignore

        path_elements = class_file_path.split(os.path.sep)
        src_index = path_elements.index("src")
        app_name = path_elements[src_index + 1]

        snake_string = re.sub(r"(?<!^)(?=[A-Z])", "_", cls.__name__).lower()

        return app_name + "_" + snake_string
