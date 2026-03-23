from sqlmodel import SQLModel
from typing import Optional


# User table
class UserDefault(SQLModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    username: str
    email: str
