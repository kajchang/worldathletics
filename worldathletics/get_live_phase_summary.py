# Generated by ariadne-codegen on 2024-06-04 14:46
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetLivePhaseSummary(BaseModel):
    get_live_phase_summary: Optional[
        List[Optional["GetLivePhaseSummaryGetLivePhaseSummary"]]
    ] = Field(alias="getLivePhaseSummary")


class GetLivePhaseSummaryGetLivePhaseSummary(BaseModel):
    id: str
    phase_summary_id: Optional[int] = Field(alias="phaseSummaryId")
    phase_id: Optional[int] = Field(alias="phaseId")
    unit_id: Optional[int] = Field(alias="unitId")
    unit_name: Optional[str] = Field(alias="unitName")
    unit_type: Optional[str] = Field(alias="unitType")
    competitor_id: Optional[int] = Field(alias="competitorId")
    competitor_team_name: Optional[str] = Field(alias="competitorTeamName")
    competitor_forename: Optional[str] = Field(alias="competitorForename")
    competitor_surname: Optional[str] = Field(alias="competitorSurname")
    competitor_country_name: Optional[str] = Field(alias="competitorCountryName")
    competitor_country_code: Optional[str] = Field(alias="competitorCountryCode")
    competitor_sex: Optional[str] = Field(alias="competitorSex")
    competitor_type: Optional[str] = Field(alias="competitorType")
    bib: Optional[str]
    rank: Optional[str]
    mark: Optional[str]
    wind: Optional[str]
    result_wind: Optional[str] = Field(alias="resultWind")
    record: Optional[str]
    qualified: Optional[str]
    combined_points: Optional[str] = Field(alias="combinedPoints")
    updated_on: Optional[str] = Field(alias="updatedOn")
    result_rank: Optional[str] = Field(alias="resultRank")
    phase_summary_order: Optional[int] = Field(alias="phaseSummaryOrder")
    provisional_qualifier: Optional[bool] = Field(alias="provisionalQualifier")
    event_store_id: Optional[str] = Field(alias="eventStoreId")
    competition_id: Optional[int] = Field(alias="competitionId")
    reaction_time: Optional[str] = Field(alias="reactionTime")
    phase_summary_milliseconds: Optional[str] = Field(alias="phaseSummaryMilliseconds")


GetLivePhaseSummary.update_forward_refs()
GetLivePhaseSummaryGetLivePhaseSummary.update_forward_refs()
