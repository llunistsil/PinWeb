from sqlmodel import Field, Relationship
from datetime import datetime
from typing import Optional, List

from src.api.notifications.default import NotificationDefault
from src.api.priorities.default import PriorityDefault
from src.api.schedule_tasks.default import ScheduleTaskDefault
from src.api.schedules.default import ScheduleDefault
from src.api.tasks.default import TaskDefault
from src.api.time_entries.default import TimeEntryDefault
from src.api.users.default import UserDefault


class ScheduleTask(ScheduleTaskDefault, table=True):
    added_at: datetime = Field(default_factory=datetime.utcnow)

class User(UserDefault, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    password_hash: Optional[str] = None
    tasks: List["Task"] = Relationship(back_populates="user",
                                       sa_relationship_kwargs={"cascade": "delete"})
    schedules: List["Schedule"] = Relationship(back_populates="user",
                                               sa_relationship_kwargs={"cascade": "delete"})

class Priority(PriorityDefault, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    tasks: List["Task"] = Relationship(back_populates="priority",
                                       sa_relationship_kwargs={"cascade": "delete"})

class Task(TaskDefault, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    priority: Optional[Priority] = Relationship(back_populates="tasks")
    user: Optional[User] = Relationship(back_populates="tasks")
    time_entries: List["TimeEntry"] = Relationship(back_populates="task",
                                                   sa_relationship_kwargs={"cascade": "delete"})
    notifications: List["Notification"] = Relationship(back_populates="task",
                                                       sa_relationship_kwargs={"cascade": "delete"})
    schedules: List["Schedule"] = Relationship(back_populates="tasks",
                                               link_model=ScheduleTask,
                                               sa_relationship_kwargs={"cascade": "delete"})

class TimeEntry(TimeEntryDefault, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    task: Optional[Task] = Relationship(back_populates="time_entries")

class Schedule(ScheduleDefault, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user: Optional[User] = Relationship(back_populates="schedules")
    tasks: List[Task] = Relationship(back_populates="schedules",
                                     link_model=ScheduleTask,
                                     sa_relationship_kwargs={"cascade": "delete"})

class Notification(NotificationDefault, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    task: Optional[Task] = Relationship(back_populates="notifications")
