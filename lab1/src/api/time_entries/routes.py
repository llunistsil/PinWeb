from fastapi import APIRouter, Depends

from src.api.generic import Response, create_object, delete_object, read_object, read_object_list, update_object
from src.api.time_entries.default import TimeEntryDefault
from src.api.time_entries.schemas import TimeEntryInner
from src.db.connection import get_session
from src.db.models import TimeEntry


router = APIRouter(prefix="/time_entries", tags=["time_entries"])


@router.post("/")
def create_time_entry(time_entry: TimeEntryDefault, session=Depends(get_session)) -> Response[TimeEntry]:
    return create_object(session, time_entry, TimeEntry)

@router.get("/")
def get_time_entries(session=Depends(get_session)) -> list[TimeEntry]:
    return read_object_list(session, TimeEntry)

@router.get("/{time_entry_id}", response_model=TimeEntryInner)
def get_time_entry(time_entry_id: int, session=Depends(get_session)) -> TimeEntry:
    return read_object(session, time_entry_id, TimeEntry)

@router.patch("/{time_entry_id}")
def update_time_entry(time_entry_id: int, time_entry: TimeEntryDefault, session=Depends(get_session)) -> TimeEntryDefault:
    return update_object(session, time_entry_id, time_entry, TimeEntry)

@router.delete("/{time_entry_id}")
def delete_time_entry(time_entry_id: int, session=Depends(get_session)) -> dict:
    return delete_object(session, time_entry_id, TimeEntry)
