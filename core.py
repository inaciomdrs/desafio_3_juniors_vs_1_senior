import pytest
from api import API_APP
from fastapi.testclient import TestClient


@pytest.fixture
def api_client():
    with open("usuarios_1000.json", "rb") as upload_file:
        files = {"users_data": upload_file}
        client = TestClient(API_APP)
        _ = client.post("/users", files=files)
        return client
