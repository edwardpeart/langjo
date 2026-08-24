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
