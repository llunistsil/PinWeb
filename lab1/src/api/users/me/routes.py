from fastapi import APIRouter, Depends

from src.auth.dependencies import AccessTokenBearer
from src.api.generic import Response
from src.api.users.me.default import UserCreate, UserLogin
from src.api.users.me.me import create_user, enter_into_user, info_user, reset_password_user
from src.api.users.me.schemas import UserJWTResponse, UserResponse
from src.db.connection import get_session


router = APIRouter(prefix="/me", tags=["me"])

@router.post("/register")
def register_user(user: UserCreate, session=Depends(get_session)) -> Response[UserJWTResponse]:
    return create_user(user, session)

@router.post("/login")
def login_user(user: UserLogin, session=Depends(get_session)) -> Response[UserJWTResponse]:
    return enter_into_user(user, session)

@router.post("/password")
def password_user(user: UserLogin, session=Depends(get_session)) -> Response[UserJWTResponse]:
    return reset_password_user(user, session)

@router.get("/")
def get_info_current_user(token=Depends(AccessTokenBearer()), session=Depends(get_session)) -> Response[UserResponse]:
    return info_user(token['sub'], session)
