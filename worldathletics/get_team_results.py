# Generated by ariadne-codegen on 2023-06-06 10:49
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetTeamResults(BaseModel):
    get_team_results: Optional[List[Optional["GetTeamResultsGetTeamResults"]]] = Field(
        alias="getTeamResults"
    )


class GetTeamResultsGetTeamResults(BaseModel):
    type: Optional[str]
    id: str
    phase_id: int = Field(alias="phaseId")
    unit_id: Optional[int] = Field(alias="unitId")
    unit_name: Optional[str] = Field(alias="unitName")
    unit_type: Optional[str] = Field(alias="unitType")
    intermediate_type: Optional[str] = Field(alias="intermediateType")
    intermediate_id: Optional[int] = Field(alias="intermediateId")
    split_name: Optional[str] = Field(alias="splitName")
    intermediate_id_type: Optional[str] = Field(alias="intermediateIdType")
    intermediate_result_order: Optional[int] = Field(alias="intermediateResultOrder")
    intermediate_order: Optional[int] = Field(alias="intermediateOrder")
    standing_points: Optional[str] = Field(alias="standingPoints")
    gap: Optional[str]
    result_id: Optional[int] = Field(alias="resultId")
    no_start: Optional[bool] = Field(alias="noStart")
    lane: Optional[str]
    season_best_mark: Optional[str] = Field(alias="seasonBestMark")
    personal_best_mark: Optional[str] = Field(alias="personalBestMark")
    phase_summary_order: Optional[int] = Field(alias="phaseSummaryOrder")
    result_ranks: Optional[int] = Field(alias="resultRanks")
    summary_yank: Optional[int] = Field(alias="summaryYank")
    competitor_id: Optional[int] = Field(alias="competitorId")
    competitor_forename: Optional[str] = Field(alias="competitorForename")
    competitor_surname: Optional[str] = Field(alias="competitorSurname")
    competitor_team_name: Optional[str] = Field(alias="competitorTeamName")
    competitor_country_name: Optional[str] = Field(alias="competitorCountryName")
    competitor_country_code: Optional[str] = Field(alias="competitorCountryCode")
    competitor_sex: Optional[str] = Field(alias="competitorSex")
    competitor_type: Optional[str] = Field(alias="competitorType")
    bib: Optional[str]
    rank: Optional[str]
    mark: Optional[str]
    combined_points: Optional[str] = Field(alias="combinedPoints")
    reaction_time: Optional[str] = Field(alias="reactionTime")
    record: Optional[str]
    result_order: Optional[int] = Field(alias="resultOrder")
    start_order: Optional[int] = Field(alias="startOrder")
    qualified: Optional[str]
    next: Optional[bool]
    last: Optional[bool]
    updated_on: Optional[str] = Field(alias="updatedOn")
    wind: Optional[str]
    team_name: Optional[str] = Field(alias="teamName")
    team_members: Optional[
        List[Optional["GetTeamResultsGetTeamResultsTeamMembers"]]
    ] = Field(alias="teamMembers")
    event_store_id: Optional[str] = Field(alias="eventStoreId")
    competition_id: Optional[int] = Field(alias="competitionId")
    result_milliseconds: Optional[str] = Field(alias="resultMilliseconds")
    world_ranking: Optional[str] = Field(alias="worldRanking")


class GetTeamResultsGetTeamResultsTeamMembers(BaseModel):
    phase_id: Optional[int] = Field(alias="phaseId")
    unit_id: Optional[int] = Field(alias="unitId")
    unit_name: Optional[str] = Field(alias="unitName")
    live_result_id: Optional[int] = Field(alias="liveResultId")
    competitor_id: Optional[int] = Field(alias="competitorId")
    competitor_forename: Optional[str] = Field(alias="competitorForename")
    competitor_surname: Optional[str] = Field(alias="competitorSurname")
    competitor_country_name: Optional[str] = Field(alias="competitorCountryName")
    competitor_country_code: Optional[str] = Field(alias="competitorCountryCode")


GetTeamResults.update_forward_refs()
GetTeamResultsGetTeamResults.update_forward_refs()
GetTeamResultsGetTeamResultsTeamMembers.update_forward_refs()
