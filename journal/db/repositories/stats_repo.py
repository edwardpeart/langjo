from sqlalchemy.orm import Session

from ..models.entry_model import Entry
from ..models.vocab_model import Vocab


class StatsRepository:
    def get_entry_count(self, db: Session):
        return db.query(Entry).count()

    def get_vocab_count(self, db: Session):
        return db.query(Vocab).count()

    def get_entries_date_desc(self, db: Session):
        return db.query(Entry).order_by(Entry.created_at.desc()).all()