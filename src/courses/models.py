from sqlalchemy import UUID, ForeignKey, String, Text, JSON
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.models import Base


class Course(Base):
    name: Mapped[str] = mapped_column(String)
    content: Mapped[str] = mapped_column(Text)
    department_name: Mapped[str] = mapped_column(ForeignKey("portals_department.name"))
    author_id: Mapped[UUID] = mapped_column(ForeignKey("users_user.id"))
    author: Mapped["User"] = relationship("User", lazy="selectin")
    department: Mapped["Department"] = relationship("Department", lazy="selectin", uselist=False)


class Test(Base):
    name: Mapped[str] = mapped_column(String)
    content: Mapped[str] = mapped_column(JSON)
    department_name: Mapped[str] = mapped_column(ForeignKey("portals_department.name"))
    author_id: Mapped[UUID] = mapped_column(ForeignKey("users_user.id"))
    author: Mapped["User"] = relationship("User", lazy="selectin")
    department: Mapped["Department"] = relationship("Department", lazy="selectin", uselist=False)


class UserCourse(Base):
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users_user.id"))
    course_id: Mapped[UUID] = mapped_column(ForeignKey("courses_course.id"))
    user: Mapped["User"] = relationship("User", lazy="selectin", back_populates="courses")


class UserTest(Base):
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users_user.id"))
    test_id: Mapped[UUID] = mapped_column(ForeignKey("courses_test.id"))
    user: Mapped["User"] = relationship("User", lazy="selectin", back_populates="tests")
