from fastapi import APIRouter, Depends

from core.error import InvalidRequest
from crud import get_crud_auth_user, CRUDAuthUser
from schemas import AuthUserCreate, AuthUserResponse
from schemas.custom_types import OAuth2PasswordRequestFormLower
from utils.password_utils import verify_password

router = APIRouter()


@router.post("/register")
async def create_user(
    data_obj: AuthUserCreate,
    crud_auth_user: CRUDAuthUser = Depends(get_crud_auth_user),
):
    query = crud_auth_user.create(data_dict=data_obj.model_dump())
    return query


@router.post("/login")
async def login_user(
    form_data: OAuth2PasswordRequestFormLower = Depends(),
    crud_auth_user: CRUDAuthUser = Depends(get_crud_auth_user),
):

    auth_user = crud_auth_user.get_by_email(email=form_data.username)
    if not auth_user:
        raise InvalidRequest("Email doesn't exist")

    if not verify_password(
        plain_password=form_data.password, hashed_password=auth_user.password
    ):
        raise InvalidRequest("Incorrect Password")

    return auth_user
