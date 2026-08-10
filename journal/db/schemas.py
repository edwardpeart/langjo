from pydantic import BaseModel

class JournalEntryBase(BaseModel):
    body: str

class JournalEntryCreate(JournalEntryBase):
    pass

class JournalEntryUpdate(JournalEntryBase):
    pass

class JournalEntryInDBBase(JournalEntryBase):
    id: int
    created_at: str
    updated_at: str

    class Config:
        orm_mode = True

class JournalEntry(JournalEntryInDBBase):
    pass