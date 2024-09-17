from fastapi import APIRouter, Depends
from core.db import get_db
from pymongo.collection import Collection
from bson import ObjectId
from crud import get_crud_auth_user, CRUDAuthUser, CRUDBook, get_crud_book
from schemas.auth_user import AuthUserCreate, BookCreate

router = APIRouter()


@router.post("/register")
async def create_user(
    data_obj: AuthUserCreate, crud_auth_user: CRUDAuthUser = Depends(get_crud_auth_user)
):
    query = crud_auth_user.create(data_dict=data_obj.model_dump())
    return query


@router.post("/books")
async def create_book(
    data_obj: BookCreate, crud_book: CRUDBook = Depends(get_crud_book)
):
    query = crud_book.create(data_dict=data_obj.model_dump())
    return query


@router.get("/get-book")
async def get_books(crud_book: CRUDBook = Depends(get_crud_book)):
    return "query"
