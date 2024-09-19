from fastapi import Depends
from crud.base import CRUDBase
from core.db import get_db
from models.book import BookModel
from schemas.book import BookCreate


class CRUDBook(CRUDBase[BookModel, BookCreate]):
    pass


def get_crud_book(db=Depends(get_db)):
    return CRUDBook(db, model=BookModel)
