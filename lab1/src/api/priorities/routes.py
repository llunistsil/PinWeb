from fastapi import APIRouter, Depends

from src.api.generic import Response, create_object, delete_object, read_object, read_object_list, update_object
from src.api.priorities.default import PriorityDefault
from src.api.priorities.schemas import PriorityInner
from src.db.connection import get_session
from src.db.models import Priority


router = APIRouter(prefix="/priorities", tags=["priorities"])


@router.post("/")
def create_priority(priority: PriorityDefault, session=Depends(get_session)) -> Response[Priority]:
    return create_object(session, priority, Priority)

@router.get("/")
def get_priorities(session=Depends(get_session)) -> list[Priority]:
    return read_object_list(session, Priority)

@router.get("/{priority_id}", response_model=PriorityInner)
def get_priority(priority_id: int, session=Depends(get_session)) -> Priority:
    return read_object(session, priority_id, Priority)

@router.patch("/{priority_id}")
def update_priority(priority_id: int, priority: PriorityDefault, session=Depends(get_session)) -> PriorityDefault:
    return update_object(session, priority_id, priority, Priority)

@router.delete("/{priority_id}")
def delete_priority(priority_id: int, session=Depends(get_session)) -> dict:
    return delete_object(session, priority_id, Priority)
