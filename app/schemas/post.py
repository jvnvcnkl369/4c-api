from pydantic import BaseModel, ConfigDict
from enum import Enum
from typing import List, Optional


class PostStatus(str, Enum):
    draft = "draft"
    published = "published"
    archived = "archived"


class PostBase(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    title: str
    content: str
    status: str


class Post(PostBase):
    id: int
    user_id: int
    tags: List["Tag"] = []
    comments: List["Comment"] = []
    user: Optional["UserBase"] = None


from .tag import Tag
from .comment import Comment
from .user import UserBase

Post.model_rebuild()
