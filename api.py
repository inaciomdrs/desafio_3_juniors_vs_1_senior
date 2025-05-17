import json
from dataclasses import dataclass
from enum import Enum
from fastapi import FastAPI, UploadFile

API_APP = FastAPI()
API_APP.memory = None
API_APP.team_insights = None


class Status(Enum):
    SUCCESS = 1
    FAIL = 2


@dataclass(frozen=True)
class Result:
    status: Status


@API_APP.post("/users")
def file_upload(users_data: UploadFile):
    API_APP.memory = json.loads(users_data.file.read())
    return {"status": Status.SUCCESS}


@API_APP.get("/superusers")
def superusers():
    return [
        user for user in API_APP.memory if user["active"] and (user["score"] >= 900)
    ]


@API_APP.get("/top-countries")
def top_countries():
    countries = {}

    for user in API_APP.memory:
        if user["active"] and (user["score"] >= 900):
            countries[user["country"]] = (
                1
                if user["country"] not in countries
                else countries[user["country"]] + 1
            )

    return [
        country[0]
        for country in sorted(countries.items(), key=lambda v: v[1])[::-1][:5]
    ]


@API_APP.get("/team-insights")
def team_insights():
    if API_APP.team_insights:
        return API_APP.team_insights

    teams = {}

    for user in API_APP.memory:
        team_name = user["team"]["name"]

        if team_name not in teams:
            teams[team_name] = {
                "Total_members": 0,
                "#Leaders": 0,
                "#Completed Projects": [],
                "%Active Members": 0,
            }

        teams[team_name]["Total_members"] += 1

        if user["active"]:
            teams[team_name]["%Active Members"] += 1

        if user["team"]["leader"]:
            teams[team_name]["#Leaders"] += 1

        for project in user["team"]["projects"]:
            if project["completed"]:
                teams[team_name]["#Completed Projects"].append(project["name"])

    for team in teams:
        teams[team]["#Completed Projects"] = len(
            set(teams[team]["#Completed Projects"])
        )
        teams[team]["%Active Members"] = round(
            (teams[team]["%Active Members"] / teams[team]["Total_members"]) * 100, 2
        )

    API_APP.team_insights = teams

    return teams
