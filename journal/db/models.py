from typing import List
from sqlalchemy import String, DateTime, func, ForeignKey
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

    def __repr__(self):
        return f"User(id={self.id}, body={self.body}, vocab={self.vocab}, created_at={self.created_at}, updated_at={self.updated_at})"

class Vocab(Base):
    __tablename__ = "vocab"

    id: Mapped[int] = mapped_column(primary_key=True)
    dict_form: Mapped[str] = mapped_column(String, unique=True)
    reading: Mapped[str] = mapped_column(String)
    entry_id: Mapped[int] = mapped_column(ForeignKey(Entry.id))
    entry: Mapped["Entry"] = relationship(back_populates="vocab")
    created_at: Mapped[DateTime] = mapped_column(
            DateTime(timezone=True),
            server_default=func.now(),
            nullable=False
            )

    def __repr__(self):
        return f"Vocab(id={self.id}, dict_form={self.dict_form}, reading={self.reading}, entry_id={self.entry_id}, entry={self.entry}, created_at={self.created_at})"
