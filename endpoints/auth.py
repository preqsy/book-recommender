from fastapi import APIRouter, Depends
from crud import get_crud_auth_user, CRUDAuthUser
from schemas import AuthUserCreate, AuthUserResponse

router = APIRouter()


@router.post("/register", response_model=AuthUserResponse)
async def create_user(
    data_obj: AuthUserCreate, crud_auth_user: CRUDAuthUser = Depends(get_crud_auth_user)
):
    query = crud_auth_user.create(data_dict=data_obj.model_dump())
    return query
