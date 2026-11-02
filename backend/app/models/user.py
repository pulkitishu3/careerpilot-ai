from datetime import datetime, timezone

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.database.connection import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, index=True, nullable=False)
    hashed_password = Column(String(255), nullable=False)

    created_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    resumes = relationship(
        "Resume",
        back_populates="user",
        cascade="all, delete-orphan"
    )

    skills = relationship(
        "UserSkill",
        back_populates="user",
        cascade="all, delete-orphan"
    )