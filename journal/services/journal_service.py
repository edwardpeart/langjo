from sqlalchemy.orm import Session

from ..db.database import SessionLocal
from ..db.repositories.entry_repo import EntryRepository
from ..db.schemas import EntryCreate, EntryUpdate


class JournalService:
    def __init__(self):
        self.repo = EntryRepository()

    def save(self, text: str):
        db: Session = SessionLocal()
        try:
            return self.repo.create_entry(db, EntryCreate(body=text))
        finally:
            db.close()

    def update(self, entry_id: int, text: str):
        db: Session = SessionLocal()
        try:
            return self.repo.update_entry(db, entry_id, EntryUpdate(body=text))
        finally:
            db.close()

    def get(self, entry_id: int):
        db: Session = SessionLocal()
        try:
            return self.repo.get_entry(db, entry_id)
        finally:
            db.close()