from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, String, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base

if TYPE_CHECKING:
    from .entry_model import Entry


class Vocab(Base):
    __tablename__ = "vocab"

    id: Mapped[int] = mapped_column(primary_key=True)
    dict_form: Mapped[str] = mapped_column(String, nullable=False)
    reading: Mapped[str] = mapped_column(String)
    entry_id: Mapped[int | None] = mapped_column(
        ForeignKey("entries.id"),
        nullable=True,
    )
    entry: Mapped["Entry | None"] = relationship(back_populates="vocab")
    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    __table_args__ = (
        UniqueConstraint("dict_form", "reading", name="uq_dict_form_reading"),
    )
