from __future__ import annotations

from typing import TYPE_CHECKING, List

from sqlalchemy import DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base

if TYPE_CHECKING:
    from .vocab_model import Vocab


class Entry(Base):
    __tablename__ = "entries"

    id: Mapped[int] = mapped_column(primary_key=True)
    body: Mapped[str] = mapped_column(String, nullable=False)
    vocab: Mapped[List["Vocab"]] = relationship(
        back_populates="entry",
        cascade="all, delete-orphan",
    )
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
    )

