from typing import List, Optional
from datetime import date

from pydantic import BaseModel, EmailStr

from models.base import PyObjectId


class AuthUserCreate(BaseModel):
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    password: str
    date_of_birth: Optional[date] = None
    phone_number: Optional[str] = None
    bio: Optional[str] = None


class AuthUserResponse(BaseModel):
    id: PyObjectId
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    date_of_birth: Optional[date] = None
    phone_number: Optional[str] = None
    bio: Optional[str] = None
