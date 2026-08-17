from pydantic import BaseModel, ConfigDict
from datetime import datetime

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

class VocabBase(BaseModel):
    dict_form: str
    reading: str

class VocabCreate(VocabBase):
    pass

class VocabRead(VocabBase):
    id: int
    entry_id: int
    created_at: datetime
    model_config = ConfigDict(from_attributes=True)