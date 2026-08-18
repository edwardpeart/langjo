from typing import List
from sqlalchemy import String, DateTime, UniqueConstraint, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import Base

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


class Vocab(Base):
    __tablename__ = "vocab"

    id: Mapped[int] = mapped_column(primary_key=True)
    dict_form: Mapped[str] = mapped_column(String, nullable=False)
    reading: Mapped[str] = mapped_column(String)
    entry_id: Mapped[int | None] = mapped_column(ForeignKey(Entry.id), nullable=True)
    entry: Mapped["Entry | None"] = relationship(back_populates="vocab")
    created_at: Mapped[DateTime] = mapped_column(
            DateTime(timezone=True),
            server_default=func.now(),
            nullable=False
            )

    __table_args__ = (
        UniqueConstraint("dict_form", "reading", name="uq_dict_form_reading"),
    )

