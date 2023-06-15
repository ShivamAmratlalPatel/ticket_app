"""Store database models."""
from sqlalchemy import Boolean, Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .commands import generate_uuid
from .database import Base


class Chapter(Base):
    """Chapter table."""

    __tablename__: str = "chapters"
    chapter_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=generate_uuid(),
    )
    chapter_name = Column(String, nullable=False, unique=True, index=True)
    is_deleted = Column(Boolean, nullable=False, default=False)

    committees = relationship("Committee", back_populates="chapters")


class Committee(Base):
    """Committee table."""

    __tablename__: str = "committees"
    committee_id = Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=generate_uuid(),
    )
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    phone = Column(String)
    chapter_id = Column(UUID(as_uuid=True), ForeignKey("chapters.id"), nullable=False)

    chapter = relationship("Chapter", back_populates="committees")
