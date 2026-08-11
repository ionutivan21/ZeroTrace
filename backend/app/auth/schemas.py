from pydantic import BaseModel, EmailStr
from typing import Optional

class RegisterIn(BaseModel):
    username: str
    email: EmailStr
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"

class LoginIn(BaseModel):
    username: str
    password: str
