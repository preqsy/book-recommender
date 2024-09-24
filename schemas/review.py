from typing import Optional
from pydantic import BaseModel

from models.base import PyObjectId


class ReviewCreate(BaseModel):
    review: str
    user_id: Optional[PyObjectId] = None
    book_id: PyObjectId
