from datetime import date

from sqlalchemy import func
from sqlalchemy.orm import Session

from journal.db.models import entry_model

from ..db.database import SessionLocal
from ..db.repositories.entry_repo import EntryRepository
from ..db.schemas import EntryCreate, EntryUpdate


class JournalService:
    def __init__(self):
        self.repo = EntryRepository()

    def save(self, text: str):
        db = SessionLocal()
        try:
            today = date.today()

            existing = (
                db.query(entry_model.Entry)
                .filter(func.date(entry_model.Entry.created_at) == today.isoformat())
                .order_by(entry_model.Entry.created_at.desc())
                .first()
            )

            if existing:
                existing.body = f"{existing.body}\n\n{text}".strip()
                db.commit()
                db.refresh(existing)
                return existing

            return self.repo.create_entry(db, EntryCreate(body=text))
        finally:
            db.close()

    def update(self, entry_id: int, text: str):
        db: Session = SessionLocal()
        try:
            return self.repo.update_entry(db, entry_id, EntryUpdate(body=text))
        finally:
            db.close()

    def get_entry(self, entry_id: int):
        db: Session = SessionLocal()
        try:
            return self.repo.get_entry(db, entry_id)
        finally:
            db.close()

    def get_all_entries(self):
        db: Session = SessionLocal()
        try:
            return self.repo.get_entries_date_desc(db)
        finally:
            db.close()