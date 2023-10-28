from sqlalchemy import UUID, ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base


class Company(Base):
    name: Mapped[str] = mapped_column(String, unique=True)
    author_id: Mapped[UUID] = mapped_column(ForeignKey("users_user.id"))


class Portal(Base):
    name: Mapped[str] = mapped_column(String, unique=True)
    address: Mapped[str] = mapped_column(String)
    phone: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String)
    inn: Mapped[str] = mapped_column(String)
    main_hex_color: Mapped[str] = mapped_column(String, nullable=True)

    admin_id: Mapped[UUID] = mapped_column(ForeignKey("users_user.id", use_alter=True))
    admin: Mapped["User"] = relationship("User", lazy="selectin", foreign_keys="Portal.admin_id")


class Department(Base):
    name: Mapped[str] = mapped_column(String, unique=True)
    portal_id: Mapped[UUID] = mapped_column(ForeignKey("portals_portal.id"))
    portal: Mapped[Portal] = relationship(Portal, lazy="selectin")
    tests: Mapped[list["Test"]] = relationship("Test", back_populates="department", lazy="selectin")


class UserDepartment(Base):
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users_user.id"))
    department_id: Mapped[UUID] = mapped_column(ForeignKey("portals_department.id"))
    user: Mapped["User"] = relationship("User", lazy="selectin")
    department: Mapped[Department] = relationship(Department, lazy="selectin")
