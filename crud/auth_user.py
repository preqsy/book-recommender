from fastapi import Depends

from db import get_db
from .base import CRUDBase


class CRUDAuthUser(CRUDBase):
    pass


def get_crud_auth_user(db=Depends(get_db)):
    return CRUDAuthUser(db, collection_name="user")
