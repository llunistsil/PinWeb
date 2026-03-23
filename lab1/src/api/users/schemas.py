from src.api.users.default import UserDefault
from src.db.models import Schedule, Task
from typing import Optional, List


class UserInner(UserDefault):
    tasks: Optional[List[Task]] = None
    schedules: Optional[List[Schedule]] = None
