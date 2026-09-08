from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict

class EntryBase(BaseModel):
    body: str

class EntryCreate(EntryBase):
    pass

class EntryUpdate(BaseModel):
    body: str | None = None

class EntryRead(EntryBase):
    id: int
    created_at: datetime
    updated_at: datetime
    model_config = ConfigDict(from_attributes=True)

class EntryCreateResponse(BaseModel):
    entry: EntryRead
    new_words_added: int

class VocabBase(BaseModel):
    dict_form: str
    reading: str
    entry_id: int | None = None

class VocabCreate(VocabBase):
    pass

class VocabRead(VocabBase):
    id: int
    entry_id: int | None = None
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)

class StatsResponse(BaseModel):
    total_entries: int
    total_vocab: int
    current_streak: int
    new_vocab_today: int

class UserBase(BaseModel):
    username: str
    email: str

class UserCreate(UserBase):
    password: str

class UserRead(UserBase):
    id: UUID
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)


class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"


class TokenData(BaseModel):
    user_id: str | None = None
    email: str | None = None