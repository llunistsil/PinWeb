from pydantic import BaseModel
from typing import Optional


class UserJWTResponse(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    password: str
    access_token: Optional[str]

class UserResponse(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
