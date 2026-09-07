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
            for word in words:
                
                payload = VocabCreate(**word, entry_id=entry_id)
                created.append(self.repo.add_vocab(db, payload))
            return created
        finally:
            db.close()

    def get_vocab(self):
        db: Session = SessionLocal()
        try:
            return self.repo.get_vocab(db)
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
