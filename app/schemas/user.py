from typing import List
from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    username: str
    email: EmailStr


class User(UserBase):
    id: int
    posts: List["Post"] = []
    comments: List["Comment"] = []

    class Config:
        from_attributes = True


from .post import Post
from .comment import Comment

User.model_rebuild()
