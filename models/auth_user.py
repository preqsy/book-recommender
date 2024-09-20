from typing import ClassVar, Optional
from datetime import date

from pydantic import EmailStr
from models.base import BaseBaseModel


class AuthUserModel(BaseBaseModel):
    __collection_name__ = "auth_users"
    EMAIL: ClassVar[str] = "email"

    username: str
    email: EmailStr
    full_name: Optional[str] = None
    password: str
    date_of_birth: Optional[date] = None
    phone_number: Optional[str] = None
    bio: Optional[str] = None
    profile_picture_url: Optional[str] = None
