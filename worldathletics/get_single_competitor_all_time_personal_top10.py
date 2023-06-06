# Generated by ariadne-codegen on 2023-06-06 10:49
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetSingleCompetitorAllTimePersonalTop10(BaseModel):
    get_single_competitor_all_time_personal_top10: Optional[
        "GetSingleCompetitorAllTimePersonalTop10GetSingleCompetitorAllTimePersonalTop10"
    ] = Field(alias="getSingleCompetitorAllTimePersonalTop10")


class GetSingleCompetitorAllTimePersonalTop10GetSingleCompetitorAllTimePersonalTop10(
    BaseModel
):
    parameters: Optional[
        "GetSingleCompetitorAllTimePersonalTop10GetSingleCompetitorAllTimePersonalTop10Parameters"
    ]
    disciplines: Optional[
        List[
            Optional[
                "GetSingleCompetitorAllTimePersonalTop10GetSingleCompetitorAllTimePersonalTop10Disciplines"
            ]
        ]
    ]
    results: Optional[
        List[
            Optional[
                "GetSingleCompetitorAllTimePersonalTop10GetSingleCompetitorAllTimePersonalTop10Results"
            ]
        ]
    ]


class GetSingleCompetitorAllTimePersonalTop10GetSingleCompetitorAllTimePersonalTop10Parameters(
    BaseModel
):
    all_time_personal_top10_discipline: Optional[int] = Field(
        alias="allTimePersonalTop10Discipline"
    )


class GetSingleCompetitorAllTimePersonalTop10GetSingleCompetitorAllTimePersonalTop10Disciplines(
    BaseModel
):
    id: Optional[int]
    name: Optional[str]


class GetSingleCompetitorAllTimePersonalTop10GetSingleCompetitorAllTimePersonalTop10Results(
    BaseModel
):
    discipline: Optional[str]
    date: Optional[str]
    competition: Optional[str]
    country: Optional[str]
    category: Optional[str]
    race: Optional[str]
    place: Optional[str]
    result: Optional[str]
    wind: Optional[str]
    drop: Optional[str]
    with_wind: Optional[bool] = Field(alias="withWind")
    with_drop: Optional[bool] = Field(alias="withDrop")
    score: Optional[int]
    records: Optional[List[Optional[str]]]
    remark: Optional[str]


GetSingleCompetitorAllTimePersonalTop10.update_forward_refs()
GetSingleCompetitorAllTimePersonalTop10GetSingleCompetitorAllTimePersonalTop10.update_forward_refs()
GetSingleCompetitorAllTimePersonalTop10GetSingleCompetitorAllTimePersonalTop10Parameters.update_forward_refs()
GetSingleCompetitorAllTimePersonalTop10GetSingleCompetitorAllTimePersonalTop10Disciplines.update_forward_refs()
GetSingleCompetitorAllTimePersonalTop10GetSingleCompetitorAllTimePersonalTop10Results.update_forward_refs()
