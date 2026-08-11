from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from ..dependencies import get_db
from .schemas import ProfileOut
from ..profiles.models import Profile

router = APIRouter()

@router.get('/{user_id}', response_model=ProfileOut)
async def get_profile(user_id: int, db: AsyncSession = Depends(get_db)):
    q = select(Profile).where(Profile.user_id == user_id)
    result = await db.execute(q)
    profile = result.scalars().first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile
