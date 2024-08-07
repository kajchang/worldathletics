# Generated by ariadne-codegen
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetSingleCompetitorMajorChampionships(BaseModel):
    get_single_competitor_major_championships: Optional[
        "GetSingleCompetitorMajorChampionshipsGetSingleCompetitorMajorChampionships"
    ] = Field(alias="getSingleCompetitorMajorChampionships")


class GetSingleCompetitorMajorChampionshipsGetSingleCompetitorMajorChampionships(
    BaseModel
):
    parameters: Optional[
        "GetSingleCompetitorMajorChampionshipsGetSingleCompetitorMajorChampionshipsParameters"
    ]
    results: Optional[
        List[
            Optional[
                "GetSingleCompetitorMajorChampionshipsGetSingleCompetitorMajorChampionshipsResults"
            ]
        ]
    ]


class GetSingleCompetitorMajorChampionshipsGetSingleCompetitorMajorChampionshipsParameters(
    BaseModel
):
    major_championships_by_category: Optional[bool] = Field(
        alias="majorChampionshipsByCategory"
    )


class GetSingleCompetitorMajorChampionshipsGetSingleCompetitorMajorChampionshipsResults(
    BaseModel
):
    category: Optional[str]
    results: Optional[
        List[
            Optional[
                "GetSingleCompetitorMajorChampionshipsGetSingleCompetitorMajorChampionshipsResultsResults"
            ]
        ]
    ]


class GetSingleCompetitorMajorChampionshipsGetSingleCompetitorMajorChampionshipsResultsResults(
    BaseModel
):
    id: Optional[int]
    discipline: Optional[str]
    competition: Optional[str]
    venue: Optional[str]
    race: Optional[str]
    place: Optional[str]
    result: Optional[str]
    with_wind: Optional[bool] = Field(alias="withWind")
    wind: Optional[str]
    with_drop: Optional[bool] = Field(alias="withDrop")
    drop: Optional[str]
    date: Optional[str]
    event_id: Optional[str] = Field(alias="eventId")
    competition_id: Optional[str] = Field(alias="competitionId")


GetSingleCompetitorMajorChampionships.model_rebuild()
GetSingleCompetitorMajorChampionshipsGetSingleCompetitorMajorChampionships.model_rebuild()
GetSingleCompetitorMajorChampionshipsGetSingleCompetitorMajorChampionshipsResults.model_rebuild()
