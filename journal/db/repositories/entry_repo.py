from sqlalchemy.orm import Session
from .. import models, schemas

class EntryRepository():
    def create_entry(db: Session, item: schemas.JournalEntryCreate):
        entry = models.Entry(body=item.body)
        db.add(entry)
        db.commit()
        db.refresh(entry)
        return entry

    def update_entry(db: Session, entry_id: int, item: schemas.JournalEntryUpdate):
        entry = db.query(models.Entry).filter(models.Entry.id == entry_id).first()
        if entry:
            entry.body += item.body
            db.commit()
            db.refresh(entry)
        return entry

    def get_entry(db: Session, entry_id: int):
        return db.query(models.Entry).filter(models.Entry.id == entry_id).first()

