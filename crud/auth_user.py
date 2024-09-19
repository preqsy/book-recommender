from fastapi import Depends

from core.db import get_db
from models.auth_user import AuthUserModel
from schemas.auth_user import AuthUserCreate
from .base import CRUDBase


class CRUDAuthUser(CRUDBase[AuthUserModel, AuthUserCreate]):
    pass


def get_crud_auth_user(db=Depends(get_db)):
    return CRUDAuthUser(db, model=AuthUserModel)
