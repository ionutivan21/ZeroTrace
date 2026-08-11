from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import User

async def get_user(db: AsyncSession, user_id: int) -> User | None:
    q = select(User).where(User.id == user_id)
    result = await db.execute(q)
    return result.scalars().first()

async def get_user_by_username(db: AsyncSession, username: str) -> User | None:
    q = select(User).where(User.username == username)
    result = await db.execute(q)
    return result.scalars().first()
