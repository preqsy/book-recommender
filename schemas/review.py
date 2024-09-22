from typing import Optional
from pydantic import BaseModel


class ReviewCreate(BaseModel):
    review: str
    user_id: Optional[str] = None
    book_id: Optional[str] = None
