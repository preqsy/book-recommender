from typing import Optional
from datetime import date

from pydantic import EmailStr
from models.base import BaseBaseModel


class AuthUserModel(BaseBaseModel):
    __collection_name__ = "auth_users"

    username: str
    email: EmailStr
    full_name: Optional[str] = None
    password: str
    date_of_birth: Optional[date] = None
    phone_number: Optional[str] = None
    bio: Optional[str] = None
    profile_picture_url: Optional[str] = None
