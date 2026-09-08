from sqlalchemy.orm import Session

from .. import schemas
from ..models import entry_model


class EntryRepository:
    def create_entry(self, db: Session, item: schemas.EntryCreate, user_id=None):
        entry = entry_model.Entry(body=item.body, user_id=user_id)
        db.add(entry)
        db.commit()
        db.refresh(entry)
        return entry

    def update_entry(self, db: Session, entry_id: int, item: schemas.EntryUpdate, user_id=None):
        query = db.query(entry_model.Entry).filter(entry_model.Entry.id == entry_id)
        if user_id is not None:
            query = query.filter(entry_model.Entry.user_id == user_id)

        entry = query.first()
        if entry:
            if item.body is not None:
                separator = "\n\n" if entry.body and not entry.body.endswith("\n") else ""
                entry.body = f"{entry.body}{separator}{item.body}".strip()
            db.commit()
            db.refresh(entry)
        return entry

    def get_entry(self, db: Session, entry_id: int, user_id=None):
        query = db.query(entry_model.Entry).filter(entry_model.Entry.id == entry_id)
        if user_id is not None:
            query = query.filter(entry_model.Entry.user_id == user_id)
        return query.first()

    def get_entries_date_desc(self, db: Session, user_id=None):
        query = db.query(entry_model.Entry).order_by(entry_model.Entry.created_at.desc())
        if user_id is not None:
            query = query.filter(entry_model.Entry.user_id == user_id)
        return query.all()