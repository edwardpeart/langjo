import hashlib

from sqlalchemy.orm import Session

from .. import schemas
from ..models import user_model


class UserRepository:
    def create_user(self, db: Session, item: schemas.UserCreate):
        password_hash = hashlib.sha256(item.password.encode()).hexdigest()
        user = user_model.User(
            username=item.username,
            email=item.email,
            password_hash=password_hash,
        )
        db.add(user)
        db.commit()
        db.refresh(user)
        return user

    def get_user_by_username(self, db: Session, username: str):
        return db.query(user_model.User).filter(user_model.User.username == username).first()

    def get_user_by_email(self, db: Session, email: str):
        return db.query(user_model.User).filter(user_model.User.email == email).first()

    def get_user_by_id(self, db: Session, user_id: str):
        return db.query(user_model.User).filter(user_model.User.id == user_id).first()

    def authenticate(self, db: Session, email: str, password: str):
        user = self.get_user_by_email(db, email)
        if user is None:
            return None
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        if user.password_hash != password_hash:
            return None
        return user

    def get_or_create_default_user(self, db: Session):
        user = self.get_user_by_username(db, "system")
        if user is not None:
            return user

        default_user = user_model.User(
            username="system",
            email="system@local",
            password_hash=hashlib.sha256(b"system-default").hexdigest(),
        )
        db.add(default_user)
        db.commit()
        db.refresh(default_user)
        return default_user