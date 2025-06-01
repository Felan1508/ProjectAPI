# tests/test_users.py
import requests

def test_get_user_success(base_url):
    response = requests.get(f"{base_url}/users/1")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == 1


def test_get_user_not_found(base_url):
    response = requests.get(f"{base_url}/users/9999")
    assert response.status_code == 404
    data = response.json()
    assert data == {}

def test_get_all_users(base_url):
    response = requests.get(f"{base_url}/users")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0
    for user in data:
        assert "id" in user
        assert "name" in user
        assert "email" in user

