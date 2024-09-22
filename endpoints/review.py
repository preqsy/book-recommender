from fastapi import APIRouter, Depends, status

from crud.review import CRUDReview, get_crud_review
from models.auth_user import AuthUserModel


router = APIRouter(prefix="/review")
