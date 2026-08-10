from sqlalchemy.orm import Session
from . import models, schemas

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

def get_entry_count(db: Session):
    return db.query(models.Entry).count()

def add_vocab(db: Session, item: schemas.VocabCreate):
    vocab = models.Vocab(dict_form=item.dict_form, reading=item.reading)
    db.add(vocab)
    db.commit()
    db.refresh(vocab)
    return vocab

def get_vocab(db: Session, vocab_id: int):
    return db.query(models.Vocab).filter(models.Vocab.id == vocab_id).first()

def get_vocab_by_entry_id(db: Session, entry_id: int):
    return db.query(models.Vocab).filter(models.Vocab.entry_id == entry_id).all()
