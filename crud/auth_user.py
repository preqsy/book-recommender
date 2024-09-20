from fastapi import Depends

from core.db import get_db
from models.auth_user import AuthUserModel
from schemas.auth_user import AuthUserCreate
from .base import CRUDBase


class CRUDAuthUser(CRUDBase[AuthUserModel, AuthUserCreate]):
    def get_by_email(self, email):
        query = self._db.find_one({AuthUserModel.EMAIL: email})
        return AuthUserModel(**query) if query else None


def get_crud_auth_user(db=Depends(get_db)):
    return CRUDAuthUser(db, model=AuthUserModel)
