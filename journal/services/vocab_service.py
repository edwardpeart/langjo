from sqlalchemy.orm import Session

from journal.db.database import SessionLocal

from ..db.repositories.vocab_repo import VocabRepository
from ..db.schemas import VocabCreate
from .parsing.japanese_parser import JapaneseParser


class VocabService:
    def __init__(self):
        self.parser = JapaneseParser()
        self.repo = VocabRepository()

    def add(self, text: str, entry_id: int | None = None):
        words = self.parser.parse(text)
        db: Session = SessionLocal()
        try:
            created = []
            seen = set()

            for word in words:
                key = (word.get("dict_form"), word.get("reading"))
                if key in seen:
                    continue
                seen.add(key)

                payload = VocabCreate(**word, entry_id=entry_id)
                new_word = self.repo.add_vocab(db, payload)
                if new_word:
                    created.append(new_word)

            return created
        finally:
            db.close()

    def get_vocab_by_id(self, vocab_id: int):
        db: Session = SessionLocal()
        try:
            return self.repo.get_vocab_by_id(db, vocab_id)
        finally:
            db.close()

    def get_vocab_by_entry_id(self, entry_id: int):
        db: Session = SessionLocal()
        try:
            return self.repo.get_vocab_by_entry_id(db, entry_id)
        finally:
            db.close()
