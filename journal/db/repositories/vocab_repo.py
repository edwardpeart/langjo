from sqlalchemy.orm import Session

from .. import schemas
from ..models import entry_model


class VocabRepository:
    def add_vocab(self, db: Session, item: schemas.VocabCreate):
        existing = (
            db.query(entry_model.Vocab)
            .filter(
                entry_model.Vocab.dict_form == item.dict_form,
                entry_model.Vocab.reading == item.reading,
            )
            .first()
        )
        if existing:
            return existing

        vocab = entry_model.Vocab(
            dict_form=item.dict_form,
            reading=item.reading,
            entry_id=item.entry_id,
        )
        db.add(vocab)
        db.commit()
        db.refresh(vocab)
        return vocab

    def get_vocab(self, db: Session, vocab_id: int):
        return db.query(entry_model.Vocab).filter(entry_model.Vocab.id == vocab_id).first()

    def get_vocab_by_entry_id(self, db: Session, entry_id: int):
        return db.query(entry_model.Vocab).filter(entry_model.Vocab.entry_id == entry_id).all()
