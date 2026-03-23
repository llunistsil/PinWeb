from fastapi import APIRouter, Depends

from src.api.generic import Response, create_object, delete_object, read_object, read_object_list, update_object
from src.api.tasks.default import TaskDefault
from src.api.tasks.schemas import TaskInner
from src.db.connection import get_session
from src.db.models import Task


router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/")
def create_task(task: TaskDefault, session=Depends(get_session)) -> Response[Task]:
    return create_object(session, task, Task)

@router.get("/")
def get_tasks(session=Depends(get_session)) -> list[Task]:
    return read_object_list(session, Task)

@router.get("/{task_id}", response_model=TaskInner)
def get_task(task_id: int, session=Depends(get_session)) -> Task:
    return read_object(session, task_id, Task)

@router.patch("/{task_id}")
def update_task(task_id: int, task: TaskDefault, session=Depends(get_session)) -> TaskDefault:
    return update_object(session, task_id, task, Task)

@router.delete("/{task_id}")
def delete_task(task_id: int, session=Depends(get_session)) -> dict:
    return delete_object(session, task_id, Task)
