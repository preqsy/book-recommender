from typing import List, Optional
from datetime import date

from pydantic import BaseModel


class BookCreate(BaseModel):
    name: str
    author: str
    published_date: Optional[date] = None
    isbn: Optional[str] = None
    genre: Optional[List[str]] = []
    summary: Optional[str] = None
    page_count: Optional[int] = None
