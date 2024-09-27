from typing import List
from pydantic import BaseModel, ConfigDict, EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr


class User(UserBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    posts: List["Post"] = []
    comments: List["Comment"] = []


from .post import Post
from .comment import Comment

User.model_rebuild()
