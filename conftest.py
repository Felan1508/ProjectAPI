# conftest.py
import pytest
import requests
import os
from dotenv import load_dotenv

load_dotenv()

@pytest.fixture(scope="session")
def base_url():
    return os.getenv("BASE_URL")

@pytest.fixture
def credentials():
    return {
        "username": os.getenv("USERNAME"),
        "password": os.getenv("PASSWORD")
    }

@pytest.fixture
def auth_url():
    return os.getenv("AUth_URL")