from pydantic import BaseModel
from enum import Enum
from typing import List, Optional


class PostStatus(str, Enum):
    draft = "draft"
    published = "published"
    archived = "archived"


class PostBase(BaseModel):
    title: str
    content: str
    status: str

    class Config:
        from_attributes = True


class Post(PostBase):
    id: int
    user_id: int
    tags: List["Tag"] | None = None
    comments: List["Comment"] | None = None
    user: Optional["UserBase"] = None


from .tag import Tag
from .comment import Comment
from .user import UserBase

Post.model_rebuild()
