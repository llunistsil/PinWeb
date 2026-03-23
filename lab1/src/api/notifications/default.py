from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional


class NotificationDefault(SQLModel):
    task_id: Optional[int] = Field(default=None, foreign_key="task.id")
    message: str
    sent_at: datetime
