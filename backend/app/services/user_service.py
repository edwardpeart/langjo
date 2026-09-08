from sqlalchemy.orm import Session

from journal.db.database import SessionLocal
from journal.db.repositories.user_repo import UserRepository
from journal.db.schemas import UserCreate


class UserService:
    def __init__(self):
        self.repo = UserRepository()

    def create_user(self, username: str, email: str, password: str):
        db: Session = SessionLocal()
        try:
            payload = UserCreate(username=username, email=email, password=password)
            return self.repo.create_user(db, payload)
        finally:
            db.close()

    def get_or_create_default_user(self, db: Session | None = None):
        if db is None:
            db = SessionLocal()
            close_db = True
        else:
            close_db = False

        try:
            user = self.repo.get_or_create_default_user(db)
            return user
        finally:
            if close_db:
                db.close()
