from models.base import BaseBaseModel


class ReviewModel(BaseBaseModel):
    review: str
    user_id: str
    book_id: str
