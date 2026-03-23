from src.api.notifications.default import NotificationDefault
from src.db.models import Task
from typing import Optional


# Notification table
class NotificationInner(NotificationDefault):
    task: Optional[Task] = None
