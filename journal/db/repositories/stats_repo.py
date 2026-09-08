from sqlalchemy.orm import Session

from ..models.entry_model import Entry
from ..models.vocab_model import Vocab


class StatsRepository:
    def get_entry_count(self, db: Session, user_id=None):
        query = db.query(Entry)
        if user_id is not None:
            query = query.filter(Entry.user_id == user_id)
        return query.count()

    def get_vocab_count(self, db: Session, user_id=None):
        query = db.query(Vocab)
        if user_id is not None:
            query = query.filter(Vocab.user_id == user_id)
        return query.count()

    def get_entries_date_desc(self, db: Session, user_id=None):
        query = db.query(Entry).order_by(Entry.created_at.desc())
        if user_id is not None:
            query = query.filter(Entry.user_id == user_id)
        return query.all()

    def get_new_vocab_count_by_date(self, db: Session, target_date, user_id=None):
        query = db.query(Vocab).filter(Vocab.created_at >= target_date)
        if user_id is not None:
            query = query.filter(Vocab.user_id == user_id)
        return query.count()