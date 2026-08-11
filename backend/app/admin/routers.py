from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from ..dependencies import get_db
from .models import AuditLog

router = APIRouter()

@router.get('/audit')
async def list_audit(db: AsyncSession = Depends(get_db)):
    q = select(AuditLog).order_by(AuditLog.created_at.desc()).limit(100)
    result = await db.execute(q)
    return result.scalars().all()
