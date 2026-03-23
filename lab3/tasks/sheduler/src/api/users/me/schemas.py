from pydantic import BaseModel
from typing import Optional


# User response with JWT model
class UserJWTResponse(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    password: str
    access_token: Optional[str]

# User response model
class UserResponse(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
