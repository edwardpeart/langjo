from datetime import date

from sqlalchemy import func
from sqlalchemy.orm import Session

from journal.db.models import entry_model
from journal.services.vocab_service import VocabService

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
            self.vocab_service.add(text, entry.id)
            return entry
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