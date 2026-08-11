from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from datetime import timedelta

from ..dependencies import get_db
from . import schemas, crud, security
from ..users.schemas import UserOut

router = APIRouter()

@router.post('/register', response_model=UserOut)
async def register(payload: schemas.RegisterIn, db: AsyncSession = Depends(get_db)):
    existing = await crud.get_user_by_username(db, payload.username)
    if existing:
        raise HTTPException(status_code=400, detail="Username already exists")
    user = await crud.create_user(db, payload.username, payload.email, payload.password)
    return user

@router.post('/login', response_model=schemas.Token)
async def login(payload: schemas.LoginIn, db: AsyncSession = Depends(get_db)):
    user = await crud.authenticate_user(db, payload.username, payload.password)
    if not user:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    access = security.create_access_token(subject=str(user.id), expires_delta=timedelta(minutes=60))
    return {"access_token": access, "token_type": "bearer"}
