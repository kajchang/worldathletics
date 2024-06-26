# Generated by ariadne-codegen on 2024-06-04 13:40
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetSingleCompetitorResultsDiscipline(BaseModel):
    get_single_competitor_results_discipline: Optional[
        "GetSingleCompetitorResultsDisciplineGetSingleCompetitorResultsDiscipline"
    ] = Field(alias="getSingleCompetitorResultsDiscipline")


class GetSingleCompetitorResultsDisciplineGetSingleCompetitorResultsDiscipline(
    BaseModel
):
    parameters: Optional[
        "GetSingleCompetitorResultsDisciplineGetSingleCompetitorResultsDisciplineParameters"
    ]
    active_years: Optional[List[Optional[str]]] = Field(alias="activeYears")
    results_by_event: Optional[
        List[
            Optional[
                "GetSingleCompetitorResultsDisciplineGetSingleCompetitorResultsDisciplineResultsByEvent"
            ]
        ]
    ] = Field(alias="resultsByEvent")
    results_by_date: Optional[
        List[
            Optional[
                "GetSingleCompetitorResultsDisciplineGetSingleCompetitorResultsDisciplineResultsByDate"
            ]
        ]
    ] = Field(alias="resultsByDate")


class GetSingleCompetitorResultsDisciplineGetSingleCompetitorResultsDisciplineParameters(
    BaseModel
):
    results_by_year: Optional[int] = Field(alias="resultsByYear")
    results_by_year_order_by: Optional[str] = Field(alias="resultsByYearOrderBy")


class GetSingleCompetitorResultsDisciplineGetSingleCompetitorResultsDisciplineResultsByEvent(
    BaseModel
):
    indoor: Optional[bool]
    discipline_code: Optional[str] = Field(alias="disciplineCode")
    discipline_name_url_slug: Optional[str] = Field(alias="disciplineNameUrlSlug")
    type_name_url_slug: Optional[str] = Field(alias="typeNameUrlSlug")
    discipline: Optional[str]
    with_wind: Optional[bool] = Field(alias="withWind")
    results: Optional[
        List[
            Optional[
                "GetSingleCompetitorResultsDisciplineGetSingleCompetitorResultsDisciplineResultsByEventResults"
            ]
        ]
    ]


class GetSingleCompetitorResultsDisciplineGetSingleCompetitorResultsDisciplineResultsByEventResults(
    BaseModel
):
    date: Optional[str]
    competition: Optional[str]
    venue: Optional[str]
    indoor: Optional[bool]
    country: Optional[str]
    category: Optional[str]
    race: Optional[str]
    place: Optional[str]
    mark: Optional[str]
    wind: Optional[str]
    not_legal: Optional[bool] = Field(alias="notLegal")
    result_score: Optional[int] = Field(alias="resultScore")
    remark: Optional[str]
    competition_id: Optional[str] = Field(alias="competitionId")
    event_id: Optional[str] = Field(alias="eventId")


class GetSingleCompetitorResultsDisciplineGetSingleCompetitorResultsDisciplineResultsByDate(
    BaseModel
):
    date: Optional[str]
    competition: Optional[str]
    venue: Optional[str]
    indoor: Optional[bool]
    country: Optional[str]
    category: Optional[str]
    race: Optional[str]
    place: Optional[str]
    mark: Optional[str]
    wind: Optional[str]
    not_legal: Optional[bool] = Field(alias="notLegal")
    result_score: Optional[int] = Field(alias="resultScore")
    remark: Optional[str]
    competition_id: Optional[str] = Field(alias="competitionId")
    event_id: Optional[str] = Field(alias="eventId")


GetSingleCompetitorResultsDiscipline.update_forward_refs()
GetSingleCompetitorResultsDisciplineGetSingleCompetitorResultsDiscipline.update_forward_refs()
GetSingleCompetitorResultsDisciplineGetSingleCompetitorResultsDisciplineParameters.update_forward_refs()
GetSingleCompetitorResultsDisciplineGetSingleCompetitorResultsDisciplineResultsByEvent.update_forward_refs()
GetSingleCompetitorResultsDisciplineGetSingleCompetitorResultsDisciplineResultsByEventResults.update_forward_refs()
GetSingleCompetitorResultsDisciplineGetSingleCompetitorResultsDisciplineResultsByDate.update_forward_refs()
