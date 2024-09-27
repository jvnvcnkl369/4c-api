from app.models import models
from app.utils import apply_includes


def test_apply_includes(db_session):
    query = db_session.query(models.Post)
    included_query = apply_includes(query, models.Post, "user,tags")
    assert "user" in str(included_query)
    assert "tags" in str(included_query)


def test_apply_includes_invalid(db_session):
    query = db_session.query(models.Post)
    included_query = apply_includes(query, models.Post, "randomWord")
    assert str(included_query) == str(query)
