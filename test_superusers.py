import pytest
from core import api_client


@pytest.fixture
def superusers_endpoint(api_client):
    return api_client.get("/superusers").json()


def test_superusers_endpoint_is_a_list_of_103_users(
    superusers_endpoint,
):
    assert type(superusers_endpoint) == list
    assert len(superusers_endpoint) == 103


def test_superusers_endpoint_list_has_the_correct_fields(superusers_endpoint):
    expected_keys = ["id", "name", "age", "score", "active", "country", "team", "logs"]

    assert all(
        [
            (len(list(e.keys())) == len(expected_keys))
            and all(
                e_key == ek_key for e_key, ek_key in zip(list(e.keys()), expected_keys)
            )
            for e in superusers_endpoint
        ]
    )
