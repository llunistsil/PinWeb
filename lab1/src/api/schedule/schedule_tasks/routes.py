from fastapi import APIRouter, Depends

from src.api.generic import Response, read_object_list
from src.api.schedule_tasks.schedule_tasks import create_st, delete_st, get_st
from src.db.connection import get_session
from src.db.models import ScheduleTask


router = APIRouter(prefix="/schedule_tasks", tags=["schedule_tasks"])


@router.post("/{schedule_id}/{task_id}")
def create_schedule_task(schedule_id: int, task_id: int, session=Depends(get_session)) -> Response[ScheduleTask]:
    return create_st(schedule_id, task_id, session)

@router.get("/")
def get_schedule_tasks(session=Depends(get_session)) -> list[ScheduleTask]:
    return read_object_list(session, ScheduleTask)

@router.get("/{schedule_id}/{task_id}")
def get_schedule_task(schedule_id: int, task_id: int, session=Depends(get_session)) -> ScheduleTask:
    return get_st(schedule_id, task_id, session)

@router.delete("/{schedule_id}/{task_id}")
def delete_schedule_task(schedule_id: int, task_id: int, session=Depends(get_session)) -> dict:
    return delete_st(schedule_id, task_id, session)
