# Generated by ariadne-codegen
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetCombinedPoints(BaseModel):
    get_combined_points: Optional["GetCombinedPointsGetCombinedPoints"] = Field(
        alias="getCombinedPoints"
    )


class GetCombinedPointsGetCombinedPoints(BaseModel):
    all_disciplines: Optional[
        List[Optional["GetCombinedPointsGetCombinedPointsAllDisciplines"]]
    ] = Field(alias="allDisciplines")
    competitors: Optional[
        List[Optional["GetCombinedPointsGetCombinedPointsCompetitors"]]
    ]


class GetCombinedPointsGetCombinedPointsAllDisciplines(BaseModel):
    discipline_order: Optional[int] = Field(alias="disciplineOrder")
    discipline_id: Optional[str] = Field(alias="disciplineId")
    discipline_name: Optional[str] = Field(alias="disciplineName")


class GetCombinedPointsGetCombinedPointsCompetitors(BaseModel):
    competitor_name: Optional[str] = Field(alias="competitorName")
    competitor_first_name: Optional[str] = Field(alias="competitorFirstName")
    competitor_last_name: Optional[str] = Field(alias="competitorLastName")
    competitor_id_wa: Optional[int] = Field(alias="competitorId_WA")
    competitor_country_code: Optional[str] = Field(alias="competitorCountryCode")
    competitor_country_name: Optional[str] = Field(alias="competitorCountryName")
    result_country_name: Optional[str] = Field(alias="resultCountryName")
    result_country_code: Optional[str] = Field(alias="resultCountryCode")
    total_result_mark: Optional[str] = Field(alias="totalResultMark")
    disciplines: Optional[
        List[Optional["GetCombinedPointsGetCombinedPointsCompetitorsDisciplines"]]
    ]


class GetCombinedPointsGetCombinedPointsCompetitorsDisciplines(BaseModel):
    result_mark: Optional[str] = Field(alias="resultMark")
    result_rank: Optional[int] = Field(alias="resultRank")
    result_order: Optional[int] = Field(alias="resultOrder")
    result_wind: Optional[str] = Field(alias="resultWind")
    summary_rank: Optional[int] = Field(alias="summaryRank")
    summary_points: Optional[int] = Field(alias="summaryPoints")
    overall_rank: Optional[int] = Field(alias="overallRank")
    record: Optional[str]
    discipline_order: Optional[int] = Field(alias="disciplineOrder")
    discipline_id: Optional[str] = Field(alias="disciplineId")
    discipline_name: Optional[str] = Field(alias="disciplineName")
    combined_points: Optional[str] = Field(alias="combinedPoints")
    points_tally: Optional[str] = Field(alias="pointsTally")


GetCombinedPoints.model_rebuild()
GetCombinedPointsGetCombinedPoints.model_rebuild()
GetCombinedPointsGetCombinedPointsCompetitors.model_rebuild()
