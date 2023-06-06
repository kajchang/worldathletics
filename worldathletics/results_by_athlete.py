# Generated by ariadne-codegen on 2023-06-06 10:50
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class ResultsByAthlete(BaseModel):
    results_by_athlete: Optional["ResultsByAthleteResultsByAthlete"] = Field(
        alias="resultsByAthlete"
    )


class ResultsByAthleteResultsByAthlete(BaseModel):
    results: Optional[List[Optional["ResultsByAthleteResultsByAthleteResults"]]]
    parameters: Optional["ResultsByAthleteResultsByAthleteParameters"]


class ResultsByAthleteResultsByAthleteResults(BaseModel):
    athlete: Optional["ResultsByAthleteResultsByAthleteResultsAthlete"]
    competition: Optional[str]
    date: Optional[str]
    discipline: Optional[str]
    mark: Optional[str]
    match_type: Optional[str] = Field(alias="matchType")
    place: Optional[str]
    race: Optional[str]
    team: Optional[str]
    venue: Optional[str]


class ResultsByAthleteResultsByAthleteResultsAthlete(BaseModel):
    birth_date: Optional[str] = Field(alias="birthDate")
    country: Optional[str]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    id: Optional[int]
    name: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")


class ResultsByAthleteResultsByAthleteParameters(BaseModel):
    athlete_ids: Optional[List[Optional[int]]] = Field(alias="athleteIds")
    country_of_residence: Optional[str] = Field(alias="countryOfResidence")
    limit: Optional[int]
    preferred_country: Optional[str] = Field(alias="preferredCountry")


ResultsByAthlete.update_forward_refs()
ResultsByAthleteResultsByAthlete.update_forward_refs()
ResultsByAthleteResultsByAthleteResults.update_forward_refs()
ResultsByAthleteResultsByAthleteResultsAthlete.update_forward_refs()
ResultsByAthleteResultsByAthleteParameters.update_forward_refs()
