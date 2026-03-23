from fastapi import APIRouter, Depends

from src.api.generic import Response, create_object, delete_object, read_object, read_object_list, update_object
from src.api.notifications.default import NotificationDefault
from src.api.notifications.schemas import NotificationInner
from src.db.connection import get_session
from src.db.models import Notification


router = APIRouter(prefix="/notifications", tags=["notifications"])


@router.post("/")
def create_notification(notification: NotificationDefault, session=Depends(get_session)) -> Response[Notification]:
    return create_object(session, notification, Notification)

@router.get("/")
def get_notifications(session=Depends(get_session)) -> list[Notification]:
    return read_object_list(session, Notification)

@router.get("/{notification_id}", response_model=NotificationInner)
def get_notification(notification_id: int, session=Depends(get_session)) -> Notification:
    return read_object(session, notification_id, Notification)

@router.patch("/{notification_id}")
def update_notification(notification_id: int, notification: NotificationDefault, session=Depends(get_session)) -> NotificationDefault:
    return update_object(session, notification_id, notification, Notification)

@router.delete("/{notification_id}")
def delete_notification(notification_id: int, session=Depends(get_session)) -> dict:
    return delete_object(session, notification_id, Notification)
