from src.api.schedules.default import ScheduleDefault
from src.db.models import Task, User
from typing import Optional, List


# Schedule table
class ScheduleInner(ScheduleDefault):
    user: Optional[User] = None
    tasks: Optional[List[Task]] = None
