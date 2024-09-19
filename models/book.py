from typing import List, Optional
from datetime import date


from models.base import BaseBaseModel


class BookModel(BaseBaseModel):
    __collection_name__ = "Books"
    name: str
    author: str
    published_date: Optional[date] = None
    isbn: Optional[str] = None
    genre: Optional[List[str]] = []
    summary: Optional[str] = None
    page_count: Optional[int] = None
