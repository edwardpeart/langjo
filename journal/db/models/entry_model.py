from typing import List
from sqlalchemy import String, DateTime, UniqueConstraint, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..database import Base

class Entry(Base):
    __tablename__ = "entries"

    id: Mapped[int] = mapped_column(primary_key=True)
    body: Mapped[str] = mapped_column(String, nullable=False)
    vocab: Mapped[List["Vocab"]] = relationship(
        back_populates="entry", cascade="all, delete-orphan"
    )
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
        )
    updated_at:Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
        )


