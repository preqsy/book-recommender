from fastapi import APIRouter, Depends, Query
from crud import CRUDBook, get_crud_book
from schemas import BookCreate

router = APIRouter(prefix="/books")


@router.post("/")
async def create_book(
    data_obj: BookCreate, crud_book: CRUDBook = Depends(get_crud_book)
):
    query = crud_book.create(data_dict=data_obj.model_dump())
    return query


@router.get("/")
async def get_books(
    limit: int = Query(default=100), crud_book: CRUDBook = Depends(get_crud_book)
):
    books = crud_book.get_multi(limit=limit)
    return books


@router.get("/{id}")
async def get_books(id: str, crud_book: CRUDBook = Depends(get_crud_book)):
    book = crud_book.get(id=id)
    return book
