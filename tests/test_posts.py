import pytest
from app.models import models


def test_get_posts(client, seed_data):
    response = client.get("/api/posts")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["title"] == "Test Post"


def test_get_posts_with_status(client, seed_data):
    response = client.get("/api/posts?status=published")
    assert response.status_code == 200
    assert response.json()[0]["status"] == "published"


def test_get_posts_with_includes(client, seed_data):
    response = client.get("/api/posts?include=tags,user")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert "tags" in response.json()[0]
    assert "user" in response.json()[0]


def test_get_posts_with_invalid_include(client, seed_data):
    response = client.get("/api/posts?include=invalid")
    assert response.status_code == 200
    assert "invalid" not in response.json()[0]


def test_get_post(client, seed_data):
    response = client.get("/api/posts/1")
    assert response.status_code == 200
    assert response.json()["title"] == "Test Post"


def test_get_post_with_includes(client, seed_data):
    response = client.get("/api/posts/1?include=tags,user,comments")
    assert response.status_code == 200
    assert "tags" in response.json()
    assert "user" in response.json()
    assert "comments" in response.json()


def test_get_post_not_found(client, seed_data):
    response = client.get("/api/posts/999")
    assert response.status_code == 404


def test_get_posts_with_status_draft(client, seed_data, test_db):
    user, _, _, _ = seed_data

    draft_post = models.Post(
        title="Draft Post",
        content="Draft Content",
        status="draft",
        user_id=user.id,
    )
    test_db.add(draft_post)
    test_db.commit()

    response = client.get("/api/posts?status=draft")
    assert response.status_code == 200
    assert len(response.json()) == 1
    assert response.json()[0]["status"] == "draft"


def test_get_posts_with_invalid_status(client, seed_data, test_db):
    user, _, _, _ = seed_data
    new_post = models.Post(
        title="Another Post",
        content="More Content",
        status="published",
        user_id=user.id,
    )
    test_db.add(new_post)
    test_db.commit()
    response = client.get("/api/posts?status=invalid")
    assert response.status_code == 200
    posts = response.json()
    all_posts = test_db.query(models.Post).all()
    assert len(posts) == len(all_posts)


@pytest.mark.parametrize(
    "include",
    [
        "tags",
        "user",
        "comments",
        "tags,user",
        "tags,comments",
        "user,comments",
        "tags,user,comments",
    ],
)
def test_get_post_with_different_includes(client, seed_data, include):
    response = client.get(f"/api/posts/1?include={include}")
    assert response.status_code == 200
    for included_item in include.split(","):
        print(included_item)
        assert included_item in response.json()
