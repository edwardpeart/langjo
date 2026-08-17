from sqlalchemy.orm import Session
from .. import models

class StatsRepository():
    def get_entry_count(db: Session):
        return db.query(models.Entry).count()

    def get_entries_date_desc(db: Session):
        return db.query(models.Entry).order_by(models.Entry.created_at.desc()).all()

    def get_vocab_count(db: Session):
        return db.query(models.Vocab).count()