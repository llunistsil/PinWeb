from fastapi import APIRouter, Depends

from src.api.generic import Response, create_object, delete_object, read_object, read_object_list, update_object
from src.api.schedules.default import ScheduleDefault
from src.api.schedules.schemas import ScheduleInner
from src.db.connection import get_session
from src.db.models import Schedule


router = APIRouter(prefix="/schedules", tags=["schedules"])


@router.post("/")
def create_schedule(schedule: ScheduleDefault, session=Depends(get_session)) -> Response[Schedule]:
    return create_object(session, schedule, Schedule)

@router.get("/")
def get_schedules(session=Depends(get_session)) -> list[Schedule]:
    return read_object_list(session, Schedule)

@router.get("/{schedule_id}", response_model=ScheduleInner)
def get_schedule(schedule_id: int, session=Depends(get_session)) -> Schedule:
    return read_object(session, schedule_id, Schedule)

@router.patch("/{schedule_id}")
def update_schedule(schedule_id: int, schedule: ScheduleDefault, session=Depends(get_session)) -> ScheduleDefault:
    return update_object(session, schedule_id, schedule, Schedule)

@router.delete("/{schedule_id}")
def delete_schedule(schedule_id: int, session=Depends(get_session)) -> dict:
    return delete_object(session, schedule_id, Schedule)
