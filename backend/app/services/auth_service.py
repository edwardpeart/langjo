from datetime import datetime, timedelta, timezone

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy.orm import Session

from journal.config import config
from journal.db.database import SessionLocal, get_db
from journal.db.repositories.user_repo import UserRepository
from journal.db.schemas import TokenData

security = HTTPBearer()


def create_access_token(subject: str, email: str) -> str:
    expires_delta = timedelta(minutes=config.ACCESS_TOKEN_EXPIRE_MINUTES)
    exp = datetime.now(timezone.utc) + expires_delta
    payload = {"sub": subject, "email": email, "exp": exp}
    return jwt.encode(payload, config.SECRET_KEY, algorithm=config.ALGORITHM)


def decode_access_token(token: str):
    try:
        return jwt.decode(token, config.SECRET_KEY, algorithms=[config.ALGORITHM])
    except jwt.PyJWTError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        ) from exc


def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db),
):
    token = credentials.credentials
    payload = decode_access_token(token)
    user_id = payload.get("sub")
    email = payload.get("email")
    if user_id is None or email is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Could not validate credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )

    user = UserRepository().get_user_by_id(db, user_id)
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
            headers={"WWW-Authenticate": "Bearer"},
        )
    return user


def login_user(email: str, password: str):
    db = SessionLocal()
    try:
        user = UserRepository().authenticate(db, email, password)
        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect email or password",
            )
        token = create_access_token(str(user.id), user.email)
        return {"access_token": token, "token_type": "bearer"}
    finally:
        db.close()
