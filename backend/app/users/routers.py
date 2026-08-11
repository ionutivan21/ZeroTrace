from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from ..dependencies import get_db
from . import schemas, crud

router = APIRouter()

@router.get('/me', response_model=schemas.UserOut)
async def read_me(dummy: str = "placeholder", db: AsyncSession = Depends(get_db)):
    # Placeholder: authentication dependency to be added in PHASE 1
    raise HTTPException(status_code=501, detail="Auth dependency not wired yet")
