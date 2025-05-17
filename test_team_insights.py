import pytest
from core import api_client


@pytest.fixture
def team_insights_endpoint(api_client):
    return api_client.get("/team-insights").json()


def test_team_insights_endpoint_gets_correct_answer(
    team_insights_endpoint,
):
    correct_answer = {
        "Backend Ninjas": {
            "Total_members": 166,
            "#Leaders": 30,
            "#Completed Projects": 5,
            "%Active Members": 85.54,
        },
        "DevOps Masters": {
            "Total_members": 219,
            "#Leaders": 30,
            "#Completed Projects": 5,
            "%Active Members": 94.06,
        },
        "Frontend Avengers": {
            "Total_members": 217,
            "#Leaders": 35,
            "#Completed Projects": 5,
            "%Active Members": 90.78,
        },
        "Fullstack Force": {
            "Total_members": 213,
            "#Leaders": 29,
            "#Completed Projects": 5,
            "%Active Members": 89.67,
        },
        "UX Wizards": {
            "Total_members": 185,
            "#Leaders": 21,
            "#Completed Projects": 5,
            "%Active Members": 91.89,
        },
    }
    
    for team, team_data in team_insights_endpoint.items():
        assert team in correct_answer
        for key, value in team_data.items():
            correct_answer[team][key] == value
