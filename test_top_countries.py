import pytest
from core import api_client


@pytest.fixture
def top_countries_endpoint(api_client):
    return api_client.get("/top-countries").json()


def test_top_countries_endpoint_is_a_list_with_the_correct_countries(
    top_countries_endpoint,
):
    assert type(top_countries_endpoint) == list
    assert len(top_countries_endpoint) == 5
    
    for country_expected, country in zip(
        ['Alemanha', 'Canadá', 'Brasil', 'México', 'França'],
        top_countries_endpoint
    ):
        assert country_expected == country