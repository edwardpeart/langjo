from sqlalchemy.orm import Session

from journal.db.models import entry_model

from .. import schemas
from ..models import vocab_model


class VocabRepository:
    def add_vocab(self, db: Session, item: schemas.VocabCreate, user_id=None):
        query = db.query(vocab_model.Vocab)
        if user_id is not None:
            query = query.filter(vocab_model.Vocab.user_id == user_id)

        existing = (
            query.filter(vocab_model.Vocab.dict_form == item.dict_form)
            .filter(vocab_model.Vocab.reading == item.reading)
            .first()
        )
        if existing:
            return None

        vocab = vocab_model.Vocab(
            dict_form=item.dict_form,
            reading=item.reading,
            entry_id=item.entry_id,
            user_id=user_id,
        )
        db.add(vocab)
        db.commit()
        db.refresh(vocab)
        return vocab

    def get_vocab(self, db: Session, user_id=None):
        query = db.query(vocab_model.Vocab).order_by(vocab_model.Vocab.sort_key)
        if user_id is not None:
            query = query.filter(vocab_model.Vocab.user_id == user_id)
        return query.all()

    def get_vocab_by_id(self, db: Session, vocab_id: int, user_id=None):
        query = db.query(vocab_model.Vocab).filter(vocab_model.Vocab.id == vocab_id)
        if user_id is not None:
            query = query.filter(vocab_model.Vocab.user_id == user_id)
        return query.first()

    def get_vocab_by_entry_id(self, db: Session, entry_id: int, user_id=None):
        query = db.query(vocab_model.Vocab).filter(vocab_model.Vocab.entry_id == entry_id)
        if user_id is not None:
            query = query.filter(vocab_model.Vocab.user_id == user_id)
        return query.all()
