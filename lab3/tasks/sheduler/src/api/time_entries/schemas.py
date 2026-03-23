from src.api.time_entries.default import TimeEntryDefault
from src.db.models import Task
from typing import Optional


# TimeEntry table
class TimeEntryInner(TimeEntryDefault):
    task: Optional[Task] = None
