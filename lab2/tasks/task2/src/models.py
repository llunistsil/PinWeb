from sqlmodel import Field, SQLModel
from typing import Optional


class WebPage(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    url: str
    title: str
