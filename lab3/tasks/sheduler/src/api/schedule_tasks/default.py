from sqlmodel import SQLModel, Field
from typing import Optional


# Associative table
class ScheduleTaskDefault(SQLModel):
    schedule_id: Optional[int] = Field(default=None, foreign_key="schedule.id", primary_key=True)
    task_id: Optional[int] = Field(default=None, foreign_key="task.id", primary_key=True)
