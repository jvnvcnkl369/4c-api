import pytest
from sqlalchemy import inspect
from sqlalchemy.orm import Session
from app.database import Base, engine


def test_get_db(db_session):
    assert isinstance(db_session, Session)


def test_create_tables():
    Base.metadata.create_all(bind=engine)
    inspector = inspect(engine)
    assert inspector.has_table("users")
    assert inspector.has_table("posts")
    assert inspector.has_table("comments")
    assert inspector.has_table("tags")


def test_db_session(db_session):
    assert db_session.is_active
