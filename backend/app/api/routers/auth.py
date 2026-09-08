from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from backend.app.db.database import get_db
from backend.app.db.schemas import Token, UserCreate, UserRead
from backend.app.services.auth_service import get_current_user, login_user
from backend.app.services.user_service import UserService

router = APIRouter()


@router.post("/signup", response_model=UserRead, status_code=status.HTTP_201_CREATED)
def signup(payload: UserCreate, db=Depends(get_db)):
    service = UserService()
    existing = service.repo.get_user_by_email(db, payload.email)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email already exists",
        )
    user = service.repo.create_user(db, payload)
    return user


@router.post("/login", response_model=Token)
def login(payload: OAuth2PasswordRequestForm = Depends()):
    return login_user(payload.username, payload.password)


@router.get("/me", response_model=UserRead)
def me(current_user=Depends(get_current_user)):
    return current_user
