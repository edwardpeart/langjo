from __future__ import annotations

from typing import TYPE_CHECKING

from sqlalchemy import UUID, DateTime, ForeignKey, String, UniqueConstraint, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.ext.hybrid import hybrid_property

from ..database import Base

if TYPE_CHECKING:
    from .entry_model import Entry
    from .user_model import User

class Vocab(Base):
    __tablename__ = "vocab"

    id: Mapped[int] = mapped_column(primary_key=True)
    dict_form: Mapped[str] = mapped_column(String, nullable=False)
    reading: Mapped[str] = mapped_column(String, nullable=False)
    entry_id: Mapped[int] = mapped_column(ForeignKey("entries.id"), nullable=False)
    user_id: Mapped[UUID] = mapped_column(ForeignKey("users.id"), nullable=False)

    entry: Mapped["Entry"] = relationship(back_populates="vocab")
    user: Mapped["User"] = relationship(back_populates="vocab")

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    @hybrid_property
    def sort_key(self):
        return self.reading

    __table_args__ = (
        UniqueConstraint("user_id", "dict_form", "reading", name="uq_user_dict_form_reading"),
    )