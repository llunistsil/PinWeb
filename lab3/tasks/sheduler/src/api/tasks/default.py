from sqlmodel import SQLModel, Field
from datetime import datetime
from typing import Optional


# Task table
class TaskDefault(SQLModel):
    description: str
    deadline: datetime
    priority_id: Optional[int] = Field(default=None, foreign_key="priority.id")
    user_id: Optional[int] = Field(default=None, foreign_key="user.id")
