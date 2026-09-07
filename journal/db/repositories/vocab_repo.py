from sqlalchemy.orm import Session

from journal.db.models import entry_model

from .. import schemas
from ..models import vocab_model


class VocabRepository:
    def add_vocab(self, db: Session, item: schemas.VocabCreate):
        existing = (
            db.query(vocab_model.Vocab)
            .filter(
                vocab_model.Vocab.dict_form == item.dict_form,
                vocab_model.Vocab.reading == item.reading,
            )
            .first()
        )
        if existing:
            return existing

        vocab = vocab_model.Vocab(
            dict_form=item.dict_form,
            reading=item.reading,
            entry_id=item.entry_id,
        )
        db.add(vocab)
        db.commit()
        db.refresh(vocab)
        return vocab

    def get_vocab(self, db: Session):
        return db.query(vocab_model.Vocab).order_by(vocab_model.Vocab.sort_key).all()

    def get_vocab_by_id(self, db: Session, vocab_id: int):
        return db.query(vocab_model.Vocab).filter(vocab_model.Vocab.id == vocab_id).first()

    def get_vocab_by_entry_id(self, db: Session, entry_id: int):
        return db.query(vocab_model.Vocab).filter(vocab_model.Vocab.entry_id == entry_id).all()
