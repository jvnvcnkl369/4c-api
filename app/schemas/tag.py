from pydantic import BaseModel, ConfigDict


class TagBase(BaseModel):
    name: str


class Tag(TagBase):
    model_config = ConfigDict(from_attributes=True)

    id: int
