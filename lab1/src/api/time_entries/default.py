from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional


class TimeEntryDefault(SQLModel):
    task_id: Optional[int] = Field(default=None, foreign_key="task.id")
    start_time: datetime
    end_time: datetime
    duration: int
