from pydantic import BaseModel
from typing import Optional

class ProfileOut(BaseModel):
    id: int
    user_id: int
    avatar: Optional[str]
    bio: Optional[str]
    level: int
    xp: float
    credits: float
    reputation: float
    title: Optional[str]

    class Config:
        orm_mode = True
