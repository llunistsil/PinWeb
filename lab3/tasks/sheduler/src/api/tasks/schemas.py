from src.api.tasks.default import TaskDefault
from src.db.models import Priority, Schedule, TimeEntry, User, Notification
from typing import Optional, List


# Task table
class TaskInner(TaskDefault):
    priority: Optional[Priority] = None
    user: Optional[User] = None
    time_entries: Optional[List[TimeEntry]] = None
    notifications: Optional[List[Notification]] = None
    schedules: Optional[List[Schedule]] = None
