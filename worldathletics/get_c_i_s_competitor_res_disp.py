# Generated by ariadne-codegen on 2023-06-06 10:49
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetCISCompetitorResDisp(BaseModel):
    get_c_i_s_competitor_res_disp: Optional[
        "GetCISCompetitorResDispGetCISCompetitorResDisp"
    ] = Field(alias="getCISCompetitorResDisp")


class GetCISCompetitorResDispGetCISCompetitorResDisp(BaseModel):
    parameters: Optional["GetCISCompetitorResDispGetCISCompetitorResDispParameters"]
    active_years: Optional[List[Optional[str]]] = Field(alias="activeYears")
    results_by_event: Optional[
        List[Optional["GetCISCompetitorResDispGetCISCompetitorResDispResultsByEvent"]]
    ] = Field(alias="resultsByEvent")
    results_by_date: Optional[
        List[Optional["GetCISCompetitorResDispGetCISCompetitorResDispResultsByDate"]]
    ] = Field(alias="resultsByDate")


class GetCISCompetitorResDispGetCISCompetitorResDispParameters(BaseModel):
    results_by_year: Optional[int] = Field(alias="resultsByYear")
    results_by_year_order_by: Optional[str] = Field(alias="resultsByYearOrderBy")


class GetCISCompetitorResDispGetCISCompetitorResDispResultsByEvent(BaseModel):
    indoor: Optional[bool]
    discipline_code: Optional[str] = Field(alias="disciplineCode")
    discipline_name_url_slug: Optional[str] = Field(alias="disciplineNameUrlSlug")
    type_name_url_slug: Optional[str] = Field(alias="typeNameUrlSlug")
    discipline: Optional[str]
    with_wind: Optional[bool] = Field(alias="withWind")
    with_remark: Optional[bool] = Field(alias="withRemark")
    results: Optional[
        List[
            Optional[
                "GetCISCompetitorResDispGetCISCompetitorResDispResultsByEventResults"
            ]
        ]
    ]


class GetCISCompetitorResDispGetCISCompetitorResDispResultsByEventResults(BaseModel):
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


class GetCISCompetitorResDispGetCISCompetitorResDispResultsByDate(BaseModel):
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


GetCISCompetitorResDisp.update_forward_refs()
GetCISCompetitorResDispGetCISCompetitorResDisp.update_forward_refs()
GetCISCompetitorResDispGetCISCompetitorResDispParameters.update_forward_refs()
GetCISCompetitorResDispGetCISCompetitorResDispResultsByEvent.update_forward_refs()
GetCISCompetitorResDispGetCISCompetitorResDispResultsByEventResults.update_forward_refs()
GetCISCompetitorResDispGetCISCompetitorResDispResultsByDate.update_forward_refs()
