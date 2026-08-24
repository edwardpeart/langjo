from sqlalchemy.orm import Session

from .. import models, schemas


class EntryRepository:
    def create_entry(self, db: Session, item: schemas.EntryCreate):
        entry = models.Entry(body=item.body)
        db.add(entry)
        db.commit()
        db.refresh(entry)
        return entry

    def update_entry(self, db: Session, entry_id: int, item: schemas.EntryUpdate):
        entry = db.query(models.Entry).filter(models.Entry.id == entry_id).first()
        if entry:
            if item.body is not None:
                separator = "\n\n" if entry.body and not entry.body.endswith("\n") else ""
                entry.body = f"{entry.body}{separator}{item.body}".strip()
            db.commit()
            db.refresh(entry)
        return entry

    def get_entry(self, db: Session, entry_id: int):
        return db.query(models.Entry).filter(models.Entry.id == entry_id).first()

    def get_entries_date_desc(self, db: Session):
        return db.query(models.Entry).order_by(models.Entry.created_at.desc()).all()