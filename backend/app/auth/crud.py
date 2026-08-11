from sqlalchemy import select
from sqlalchemy.exc import NoResultFound
from sqlalchemy.ext.asyncio import AsyncSession

from ..users.models import User
from .security import hash_password, verify_password

async def create_user(db: AsyncSession, username: str, email: str, password: str, role: str = "PLAYER") -> User:
    user = User(username=username, email=email.lower(), hashed_password=hash_password(password), role=role)
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user

async def get_user_by_username(db: AsyncSession, username: str) -> User | None:
    q = select(User).where(User.username == username)
    result = await db.execute(q)
    return result.scalars().first()

async def authenticate_user(db: AsyncSession, username: str, password: str) -> User | None:
    user = await get_user_by_username(db, username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user
