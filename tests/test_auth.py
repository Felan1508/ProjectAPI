import requests
import pytest

import requests

def test_login_success(auth_url, credentials):
    response = requests.post(f"{auth_url}/auth/login", json=credentials)
    assert response.status_code == 200
    data = response.json()
    assert "accessToken" in data


def test_access_protected_route(auth_url, credentials):
    # Login and get token
    login_res = requests.post(f"{auth_url}/auth/login", json=credentials)
    token = login_res.json().get("accessToken")
    assert token is not None

    # Access protected route with token
    headers = {"Authorization": f"Bearer {token}"}
    response = requests.get(f"{auth_url}/auth/me", headers=headers)
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == credentials["username"]


def test_login_invalid_credentials(auth_url):
    credentials = {"username": "wrong", "password": "wrong"}
    response = requests.post(f"{auth_url}/auth/login", json=credentials)
    assert response.status_code == 401 or 403
