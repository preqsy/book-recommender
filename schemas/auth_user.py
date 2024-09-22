from typing import ClassVar, List, Optional
from datetime import date

from pydantic import BaseModel, EmailStr, model_validator

from models.base import PyObjectId
from utils.password_utils import hash_password


class AuthUserCreate(BaseModel):
    PASSWORD: ClassVar[str] = "password"
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    password: str
    date_of_birth: Optional[date] = None
    phone_number: Optional[str] = None
    bio: Optional[str] = None

    @model_validator(mode="before")
    @classmethod
    def hash_user_password(cls, values):
        password = values.get(cls.PASSWORD)

        values[cls.PASSWORD] = hash_password(password)

        return values


class AuthUserResponse(BaseModel):
    id: PyObjectId
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    date_of_birth: Optional[date] = None
    phone_number: Optional[str] = None
    bio: Optional[str] = None
