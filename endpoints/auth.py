from fastapi import APIRouter, Depends

from core.errors import InvalidRequest
from core.tokens import generate_access_token, get_current_user
from crud import get_crud_auth_user, CRUDAuthUser
from models.auth_user import AuthUserModel
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
    access_token = generate_access_token({"user_id": auth_user.id})
    return {"access_token": access_token}


@router.get("/me")
async def get_me(
    current_user: AuthUserModel = Depends(get_current_user),
    crud_auth_user: CRUDAuthUser = Depends(get_crud_auth_user),
):
    return crud_auth_user.get(current_user.id)
