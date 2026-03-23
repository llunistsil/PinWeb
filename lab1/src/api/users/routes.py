from fastapi import APIRouter, Depends

from src.api.generic import Response, create_object, delete_object, read_object, read_object_list, update_object
from src.api.users.default import UserDefault
from src.api.users.schemas import UserInner
from src.db.connection import get_session
from src.db.models import User

from src.api.users.me import routes as me


router = APIRouter(prefix="/users", tags=["users"])


router.include_router(me.router)


@router.post("/")
def create_user(user: UserDefault, session=Depends(get_session)) -> Response[User]:
    return create_object(session, user, User)

@router.get("/")
def get_users(session=Depends(get_session)) -> list[User]:
    return read_object_list(session, User)

@router.get("/{user_id}", response_model=UserInner)
def get_user(user_id: int, session=Depends(get_session)) -> User:
    return read_object(session, user_id, User)

@router.patch("/{user_id}")
def update_user(user_id: int, user: UserDefault, session=Depends(get_session)) -> UserDefault:
    return update_object(session, user_id, user, User)

@router.delete("/{user_id}", response_model=dict)
def delete_user(user_id: int, session=Depends(get_session)) -> dict:
    return delete_object(session, user_id, User)
