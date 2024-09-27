import pytest
from sqlalchemy import inspect
from sqlalchemy.orm import Session
from app.database import get_db, Base, engine


def test_get_db():
    db = next(get_db())
    assert isinstance(db, Session)
    db.close()


def test_create_tables():
    Base.metadata.create_all(bind=engine)
    inspector = inspect(engine)
    assert inspector.has_table("users")
    assert inspector.has_table("posts")
    assert inspector.has_table("comments")
    assert inspector.has_table("tags")


@pytest.fixture(scope="function")
def db():
    Base.metadata.create_all(bind=engine)
    yield from get_db()
    Base.metadata.drop_all(bind=engine)


def test_db_session(db):
    assert db.is_active
