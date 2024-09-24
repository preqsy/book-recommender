from models.base import BaseBaseModel, PyObjectId


class ReviewModel(BaseBaseModel):
    __collection_name__ = "reviews"
    review: str
    user_id: PyObjectId
    book_id: PyObjectId
