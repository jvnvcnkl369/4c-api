from pydantic import BaseModel, ConfigDict


class CommentBase(BaseModel):
    content: str


class Comment(CommentBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
    post_id: int
    user_id: int
