import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.main import app
from app.database import Base, get_db
from app.models import models

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    connection = engine.connect()
    transaction = connection.begin()
    session = TestingSessionLocal(bind=connection)

    yield session

    session.close()
    transaction.rollback()
    connection.close()
    Base.metadata.drop_all(bind=engine)


@pytest.fixture(scope="function")
def client(db_session):
    def override_get_db():
        try:
            yield db_session
        finally:
            pass

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as test_client:
        yield test_client


@pytest.fixture(scope="function")
def seed_data(db_session):
    user = models.User(id=1, username="testuser", email="test@example.com")
    db_session.add(user)
    db_session.commit()

    post = models.Post(
        id=1,
        title="Test Post",
        content="Test Content",
        status="published",
        user_id=user.id,
    )
    db_session.add(post)
    db_session.commit()

    comment = models.Comment(
        id=1, content="Test Comment", post_id=post.id, user_id=user.id
    )
    db_session.add(comment)
    db_session.commit()

    tag = models.Tag(id=1, name="TestTag")
    db_session.add(tag)
    db_session.commit()

    post.tags.append(tag)
    db_session.commit()

    return user, post, comment, tag


@pytest.fixture(scope="function")
def test_db(client, db_session):
    yield db_session
