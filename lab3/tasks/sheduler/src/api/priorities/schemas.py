from src.api.priorities.default import PriorityDefault
from src.db.models import Task
from typing import Optional, List


# Priority table
class PriorityInner(PriorityDefault):
    tasks: Optional[List[Task]] = None
