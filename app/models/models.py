from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from app.database import Base

post_tag = Table(
    "post_tag",
    Base.metadata,
    Column("post_id", Integer, ForeignKey("posts.id")),
    Column("tag_id", Integer, ForeignKey("tags.id")),
)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)

    posts = relationship("Post", back_populates="user", lazy="noload")
    comments = relationship("Comment", back_populates="user", lazy="noload")


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    status = Column(String)
    user_id = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="posts", lazy="noload")
    comments = relationship("Comment", back_populates="post", lazy="noload")
    tags = relationship(
        "Tag", secondary=post_tag, back_populates="posts", lazy="noload"
    )


class Comment(Base):
    __tablename__ = "comments"

    id = Column(Integer, primary_key=True)
    content = Column(String)
    post_id = Column(Integer, ForeignKey("posts.id"))
    user_id = Column(Integer, ForeignKey("users.id"))

    post = relationship("Post", back_populates="comments", lazy="noload")
    user = relationship("User", back_populates="comments", lazy="noload")


class Tag(Base):
    __tablename__ = "tags"

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)

    posts = relationship(
        "Post", secondary=post_tag, back_populates="tags", lazy="noload"
    )
