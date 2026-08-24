from sqlalchemy.orm import Session

from ..models import entry_model


class StatsRepository:
    def get_entry_count(self, db: Session):
        return db.query(entry_model.Entry).count()

    def get_vocab_count(self, db: Session):
        return db.query(entry_model.Vocab).count()