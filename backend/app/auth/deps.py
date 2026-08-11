from typing import Optional
from fastapi import Depends, HTTPException
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from sqlalchemy.ext.asyncio import AsyncSession

from ..auth.security import decode_token
from ..users.crud import get_user
from ..dependencies import get_db

security = HTTPBearer()

async def get_current_user(credentials: HTTPAuthorizationCredentials = Depends(security), db: AsyncSession = Depends(get_db)):
    token = credentials.credentials
    payload = decode_token(token)
    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    user_id = int(payload.get('sub'))
    user = await get_user(db, user_id)
    if not user or not user.is_active:
        raise HTTPException(status_code=401, detail="Inactive user")
    return user

def role_required(*allowed_roles):
    async def role_dependency(user = Depends(get_current_user)):
        if user.role.value not in allowed_roles:
            raise HTTPException(status_code=403, detail="Forbidden")
        return user
    return role_dependency
