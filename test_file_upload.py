import pytest
from fastapi.testclient import TestClient
from api import Status
from api import API_APP


@pytest.fixture
def file_upload_result():
    with open("usuarios_1000.json", "rb") as upload_file:
        files = {"users_data": upload_file}
        client = TestClient(API_APP)
        response = client.post("/users", files=files)
        response_json = response.json()
        result_status = response_json["status"]
        return result_status, API_APP.memory



def test_file_upload_is_successful(file_upload_result):
    result, _ = file_upload_result
    assert result == Status.SUCCESS.value


def test_content_of_uploaded_file_is_in_memory(file_upload_result):
    _, memory = file_upload_result
    assert memory is not None
    assert type(memory) == list


def test_content_of_uploaded_file_matches_specifications(file_upload_result):
    _, data = file_upload_result

    assert type(data) == list
    assert len(data) == 1000
    assert all([type(e) == dict for e in data])

    expected_keys = ["id", "name", "age", "score", "active", "country", "team", "logs"]

    assert all(
        [
            (len(list(e.keys())) == len(expected_keys))
            and all(
                e_key == ek_key for e_key, ek_key in zip(list(e.keys()), expected_keys)
            )
            for e in data
        ]
    )