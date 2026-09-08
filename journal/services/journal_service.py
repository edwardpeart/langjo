from datetime import date

from sqlalchemy import func
from sqlalchemy.orm import Session

from journal.services.vocab_service import VocabService
from ..db.schemas import EntryCreateResponse

from ..db.database import SessionLocal
from ..db.repositories.entry_repo import EntryRepository
from ..db.schemas import EntryCreate, EntryUpdate


class JournalService:
    def __init__(self):
        self.entry_repo = EntryRepository()
        self.vocab_service = VocabService()

    def save_entry(self, entry_id: int | None, text: str):
        db = SessionLocal()
        try:
            if entry_id is not None:
                entry = self.entry_repo.update_entry(db, entry_id, EntryUpdate(body=text))
            else:
                entry = self.entry_repo.create_entry(db, EntryCreate(body=text))
            created = self.vocab_service.add(text, entry_id=entry.id)
            return EntryCreateResponse(
                entry=entry, new_words_added=len(created)
            )
        finally:
            db.close()

    def get_entry(self, entry_id: int):
        db: Session = SessionLocal()
        try:
            return self.entry_repo.get_entry(db, entry_id)
        finally:
            db.close()

    def get_all_entries(self):
        db: Session = SessionLocal()
        try:
            return self.entry_repo.get_entries_date_desc(db)
        finally:
            db.close()