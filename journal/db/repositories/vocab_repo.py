from sqlalchemy.orm import Session

from .. import models, schemas


class VocabRepository:
    def add_vocab(self, db: Session, item: schemas.VocabCreate):
        existing = (
            db.query(models.Vocab)
            .filter(
                models.Vocab.dict_form == item.dict_form,
                models.Vocab.reading == item.reading,
            )
            .first()
        )
        if existing:
            return existing

        vocab = models.Vocab(
            dict_form=item.dict_form,
            reading=item.reading,
            entry_id=item.entry_id,
        )
        db.add(vocab)
        db.commit()
        db.refresh(vocab)
        return vocab

    def get_vocab(self, db: Session, vocab_id: int):
        return db.query(models.Vocab).filter(models.Vocab.id == vocab_id).first()

    def get_vocab_by_entry_id(self, db: Session, entry_id: int):
        return db.query(models.Vocab).filter(models.Vocab.entry_id == entry_id).all()

    def get_vocab_count(self, db: Session):
        return db.query(models.Vocab).count()
