from bson import ObjectId
from fastapi import APIRouter, Depends, status

from core.tokens import get_current_user
from crud import CRUDReview, CRUDBook, get_crud_book, get_crud_review
from models.auth_user import AuthUserModel
from schemas import ReviewCreate

router = APIRouter(prefix="/review")


@router.post("")
async def create_review(
    data_obj: ReviewCreate,
    crud_review: CRUDReview = Depends(get_crud_review),
    crud_book: CRUDBook = Depends(get_crud_book),
    current_user: AuthUserModel = Depends(get_current_user),
):
    crud_book.get_or_raise_exception(id=data_obj.book_id)
    data_obj.user_id = ObjectId(current_user.id)
    data_obj.book_id = ObjectId(data_obj.book_id)
    new_review = crud_review.create(data_obj.model_dump())

    return new_review
