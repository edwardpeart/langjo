from __future__ import annotations

from datetime import datetime
from typing import List, Optional
from uuid import UUID

from pydantic import BaseModel, ConfigDict


def _to_camel(s: str) -> str:
    parts = s.split("_")
    return parts[0] + "".join(p.title() for p in parts[1:])


class CamelModel(BaseModel):
    model_config = ConfigDict(from_attributes=True, alias_generator=_to_camel, populate_by_name=True)


# Core entry models
class EntryBase(CamelModel):
    body: str


class EntryCreate(EntryBase):
    pass


class EntryUpdate(CamelModel):
    id: int
    body: Optional[str] = None


class EntryRead(EntryBase):
    id: int
    created_at: datetime
    updated_at: datetime


# Vocab models
class VocabBase(CamelModel):
    dict_form: str
    reading: str
    entry_id: Optional[int] = None


class VocabCreate(VocabBase):
    pass


class VocabRead(VocabBase):
    id: int
    entry_id: Optional[int] = None
    created_at: datetime


# User models
class UserBase(CamelModel):
    username: str
    email: str


class UserCreate(UserBase):
    password: str


class UserRead(UserBase):
    id: UUID
    created_at: datetime


# Auth/token models
class Token(CamelModel):
    access_token: str
    token_type: str = "bearer"
    refresh_token: Optional[str] = None


class TokenData(CamelModel):
    user_id: Optional[str] = None
    email: Optional[str] = None


# Auth response including user + tokens for signup
class AuthResponse(CamelModel):
    user: UserRead
    access_token: str
    token_type: str = "bearer"
    refresh_token: Optional[str] = None


# Request model for refresh endpoint
class RefreshRequest(CamelModel):
    refresh_token: str


# Response shapes
class EntryCreateResponse(CamelModel):
    entry: EntryRead
    new_words_added: int


class VocabReadResponse(CamelModel):
    id: int
    entry_id: Optional[int] = None
    created_at: datetime


class StatsResponse(CamelModel):
    total_entries: int
    total_vocab: int
    current_streak: int
    new_vocab_today: int


# Tree node for sidebar
class EntryNode(CamelModel):
    id: int
    title: str
    preview: Optional[str] = None
    slug: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None
    has_children: bool = False
    children: Optional[List["EntryNode"]] = None


class EntryTreeResponse(CamelModel):
    __root__: List[EntryNode]
