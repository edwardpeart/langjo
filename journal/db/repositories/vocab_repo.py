from sqlalchemy.orm import Session
from .. import models, schemas

class VocabRepository():
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
