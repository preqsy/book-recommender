from fastapi import Depends
from core.db import get_db
from crud.base import CRUDBase
from models.review import ReviewModel
from schemas.review import ReviewCreate


class CRUDReview(CRUDBase[ReviewModel, ReviewCreate]):
    pass


def get_crud_review(db=Depends(get_db)) -> CRUDReview:
    return CRUDReview(db=db, model=ReviewModel)
