from sqlalchemy.orm import Session

from backend.app.db.database import SessionLocal

from ..db.repositories.vocab_repo import VocabRepository
from ..db.schemas import VocabCreate
from .parsing.japanese_parser import JapaneseParser
from .user_service import UserService


class VocabService:
    def __init__(self):
        self.parser = JapaneseParser()
        self.repo = VocabRepository()
        self.user_service = UserService()

    def add(self, text: str, entry_id: int | None = None, user_id=None):
        words = self.parser.parse(text)
        db: Session = SessionLocal()
        try:
            if user_id is None:
                user = self.user_service.get_or_create_default_user(db)
                user_id = user.id

            created = []
            seen = set()

            for word in words:
                key = (word.get("dict_form"), word.get("reading"))
                if key in seen:
                    continue
                seen.add(key)

                payload = VocabCreate(**word, entry_id=entry_id)
                new_word = self.repo.add_vocab(db, payload, user_id=user_id)
                if new_word:
                    created.append(new_word)

            return created
        finally:
            db.close()

    def get_vocab(self, user_id=None):
        db: Session = SessionLocal()
        try:
            return self.repo.get_vocab(db, user_id=user_id)
        finally:
            db.close()

    def get_vocab_by_id(self, vocab_id: int, user_id=None):
        db: Session = SessionLocal()
        try:
            return self.repo.get_vocab_by_id(db, vocab_id, user_id=user_id)
        finally:
            db.close()

    def get_vocab_by_entry_id(self, entry_id: int, user_id=None):
        db: Session = SessionLocal()
        try:
            return self.repo.get_vocab_by_entry_id(db, entry_id, user_id=user_id)
        finally:
            db.close()
