from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional


class ScheduleDefault(SQLModel):
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
    date: datetime
