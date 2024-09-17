from fastapi import Depends
from crud.base import CRUDBase
from db import get_db


class CRUDBook(CRUDBase):
    pass


def get_crud_book(db=Depends(get_db)):
    return CRUDBook(db, collection_name="books")
