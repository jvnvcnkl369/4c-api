def test_get_user(client, seed_data):
    response = client.get("/api/users/1")
    assert response.status_code == 200
    assert response.json()["username"] == "testuser"


def test_get_user_with_includes(client, seed_data):
    response = client.get("/api/users/1?include=posts,comments")
    assert response.status_code == 200
    assert "posts" in response.json()
    assert "comments" in response.json()


def test_get_user_not_found(client, seed_data):
    response = client.get("/api/users/999")
    assert response.status_code == 404
