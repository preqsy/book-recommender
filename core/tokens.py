from datetime import datetime, timedelta

from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
import jwt
from core.config import settings
from core.errors import InvalidRequest
from crud.auth_user import CRUDAuthUser, get_crud_auth_user


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login")


def generate_access_token(data_to_encode: dict):

    expiration_time = datetime.utcnow() + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRY_TIME
    )
    data_to_encode.update({"exp": expiration_time})
    return jwt.encode(
        algorithm=settings.ALGORITHM, payload=data_to_encode, key=settings.SECRET_KEY
    )


def verify_access_token(token: str, credential_exception):
    try:
        payload = jwt.decode(jwt=token, key=settings.SECRET_KEY, algorithms=["HS256"])
        if not payload["user_id"]:
            raise InvalidRequest("Invalid Token")
    except jwt.InvalidTokenError:
        raise credential_exception

    return payload


def get_current_user(
    token: str = Depends(oauth2_scheme),
    crud_auth_user: CRUDAuthUser = Depends(get_crud_auth_user),
):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid Token",
        headers={"WWW-Authenticate": "Bearer"},
    )
    token = verify_access_token(token=token, credential_exception=credential_exception)
    auth_user = crud_auth_user.get(id=token["user_id"])
    return auth_user
