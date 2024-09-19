from fastapi import APIRouter, Depends
from crud import CRUDBook, get_crud_book
from schemas import BookCreate

router = APIRouter(prefix="/books")


@router.post("/")
async def create_book(
    data_obj: BookCreate, crud_book: CRUDBook = Depends(get_crud_book)
):
    query = crud_book.create(data_dict=data_obj.model_dump())
    return query


@router.get("/get-book")
async def get_books(crud_book: CRUDBook = Depends(get_crud_book)):
    return "query"
