from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    UniqueConstraint
)
from sqlalchemy.orm import relationship

from app.database.connection import Base


class Skill(Base):
    __tablename__ = "skills"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)

    users = relationship("UserSkill", back_populates="skill")


class UserSkill(Base):
    __tablename__ = "user_skills"

    id = Column(Integer, primary_key=True, index=True)

    user_id = Column(
        Integer,
        ForeignKey("users.id"),
        nullable=False
    )

    skill_id = Column(
        Integer,
        ForeignKey("skills.id"),
        nullable=False
    )

    proficiency = Column(String(50), nullable=True)

    user = relationship("User", back_populates="skills")
    skill = relationship("Skill", back_populates="users")

    __table_args__ = (
        UniqueConstraint("user_id", "skill_id"),
    )