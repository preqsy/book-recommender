from typing import List, Optional
from datetime import date

from pydantic import BaseModel


class AuthUserCreate(BaseModel):
    username: str
    age: int


class BookCreate(BaseModel):
    name: str
    author: str
    published_date: Optional[date] = None
    ISBN: Optional[str] = None
    genre: Optional[List[str]] = []
    summary: Optional[str] = None
    language: Optional[str] = "English"
    page_count: Optional[int] = None
    publisher: Optional[str] = None
    cover_image_url: Optional[str] = None
    tags: Optional[List[str]] = []
