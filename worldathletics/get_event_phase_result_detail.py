# Generated by ariadne-codegen on 2023-06-06 10:49
# Source: graphql/queries.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetEventPhaseResultDetail(BaseModel):
    get_event_phase_result_detail: Optional[
        List[Optional["GetEventPhaseResultDetailGetEventPhaseResultDetail"]]
    ] = Field(alias="getEventPhaseResultDetail")


class GetEventPhaseResultDetailGetEventPhaseResultDetail(BaseModel):
    id: Optional[int]
    updated_on: Optional[Any] = Field(alias="updatedOn")
    hash: Optional[str]
    phase_code: Optional[str] = Field(alias="phaseCode")
    phase_name: Optional[str] = Field(alias="phaseName")
    combined_type: Optional[str] = Field(alias="combinedType")
    event_i_d: Optional[int] = Field(alias="eventID")
    phase_date_and_time: Optional[Any] = Field(alias="phaseDateAndTime")
    sex_code: Optional[str] = Field(alias="sexCode")
    sex_name: Optional[str] = Field(alias="sexName")
    discipline: Optional["GetEventPhaseResultDetailGetEventPhaseResultDetailDiscipline"]
    is_startlist_published: Optional[bool] = Field(alias="isStartlistPublished")
    is_result_published: Optional[bool] = Field(alias="isResultPublished")
    is_phase_summary_published: Optional[bool] = Field(alias="isPhaseSummaryPublished")
    is_team_standing_published: Optional[bool] = Field(alias="isTeamStandingPublished")
    combined_discipline_order: Optional[int] = Field(alias="combinedDisciplineOrder")
    phase_order: Optional[int] = Field(alias="phaseOrder")
    phase_session_name: Optional[str] = Field(alias="phaseSessionName")
    phase_session_order: Optional[int] = Field(alias="phaseSessionOrder")
    status: Optional[int]
    has_time: Optional[bool] = Field(alias="hasTime")
    event_id__w_a: Optional[int] = Field(alias="eventId_WA")
    primary_phase_order: Optional[int] = Field(alias="primaryPhaseOrder")
    is_points_published: Optional[bool] = Field(alias="isPointsPublished")
    phase_name_url_slug: Optional[str] = Field(alias="phaseNameUrlSlug")
    sex_name_url_slug: Optional[str] = Field(alias="sexNameUrlSlug")
    result: Optional["GetEventPhaseResultDetailGetEventPhaseResultDetailResult"]


class GetEventPhaseResultDetailGetEventPhaseResultDetailDiscipline(BaseModel):
    updated_on: Optional[Any] = Field(alias="updatedOn")
    hash: Optional[str]
    id: Optional[str] = Field(alias="_id")
    name: Optional[str]
    type_code: Optional[str] = Field(alias="typeCode")
    type_name: Optional[str] = Field(alias="typeName")
    type_order: Optional[int] = Field(alias="typeOrder")
    order: Optional[int]
    is_track: Optional[bool] = Field(alias="isTrack")
    is_field: Optional[bool] = Field(alias="isField")
    is_road: Optional[bool] = Field(alias="isRoad")
    is_combined: Optional[bool] = Field(alias="isCombined")
    is_walk: Optional[bool] = Field(alias="isWalk")
    is_indoor: Optional[bool] = Field(alias="isIndoor")
    is_reaction: Optional[bool] = Field(alias="isReaction")
    is_outdoor: Optional[bool] = Field(alias="isOutdoor")
    is_wind: Optional[bool] = Field(alias="isWind")
    is_relay: Optional[bool] = Field(alias="isRelay")
    is_valid_i_a_a_f: Optional[bool] = Field(alias="isValidIAAF")
    name_url_slug: Optional[str] = Field(alias="nameUrlSlug")
    type_name_url_slug: Optional[str] = Field(alias="typeNameUrlSlug")


class GetEventPhaseResultDetailGetEventPhaseResultDetailResult(BaseModel):
    id: Optional[int]
    updated_on: Optional[Any] = Field(alias="updatedOn")
    competitor_id: Optional[int] = Field(alias="competitorId")
    team_id: Optional[int] = Field(alias="teamId")
    competitor_name: Optional[str] = Field(alias="competitorName")
    competitor_country_code: Optional[str] = Field(alias="competitorCountryCode")
    competitor_country_name: Optional[str] = Field(alias="competitorCountryName")
    competitor_birth_date: Optional[str] = Field(alias="competitorBirthDate")
    competitor_type_code: Optional[str] = Field(alias="competitorTypeCode")
    result_country_code: Optional[str] = Field(alias="resultCountryCode")
    result_mark: Optional[str] = Field(alias="resultMark")
    result_rank: Optional[int] = Field(alias="resultRank")
    result_order: Optional[int] = Field(alias="resultOrder")
    unit_id: Optional[int] = Field(alias="unitId")
    unit_code: Optional[str] = Field(alias="unitCode")
    unit_name: Optional[str] = Field(alias="unitName")
    unit_type_code: Optional[str] = Field(alias="unitTypeCode")
    unit_date_and_time: Optional[Any] = Field(alias="unitDateAndTime")
    event_i_d: Optional[int] = Field(alias="eventID")
    phase_i_d: Optional[int] = Field(alias="phaseID")
    standing_points: Optional[str] = Field(alias="standingPoints")
    discipline: Optional[
        "GetEventPhaseResultDetailGetEventPhaseResultDetailResultDiscipline"
    ]
    competitor_first_name: Optional[str] = Field(alias="competitorFirstName")
    competitor_last_name: Optional[str] = Field(alias="competitorLastName")
    result_country_name: Optional[str] = Field(alias="resultCountryName")


class GetEventPhaseResultDetailGetEventPhaseResultDetailResultDiscipline(BaseModel):
    updated_on: Optional[Any] = Field(alias="updatedOn")
    hash: Optional[str]
    id: Optional[str] = Field(alias="_id")
    name: Optional[str]
    type_code: Optional[str] = Field(alias="typeCode")
    type_name: Optional[str] = Field(alias="typeName")
    type_order: Optional[int] = Field(alias="typeOrder")
    order: Optional[int]
    is_track: Optional[bool] = Field(alias="isTrack")
    is_field: Optional[bool] = Field(alias="isField")
    is_road: Optional[bool] = Field(alias="isRoad")
    is_combined: Optional[bool] = Field(alias="isCombined")
    is_walk: Optional[bool] = Field(alias="isWalk")
    is_indoor: Optional[bool] = Field(alias="isIndoor")
    is_reaction: Optional[bool] = Field(alias="isReaction")
    is_outdoor: Optional[bool] = Field(alias="isOutdoor")
    is_wind: Optional[bool] = Field(alias="isWind")
    is_relay: Optional[bool] = Field(alias="isRelay")
    is_valid_i_a_a_f: Optional[bool] = Field(alias="isValidIAAF")
    name_url_slug: Optional[str] = Field(alias="nameUrlSlug")
    type_name_url_slug: Optional[str] = Field(alias="typeNameUrlSlug")


GetEventPhaseResultDetail.update_forward_refs()
GetEventPhaseResultDetailGetEventPhaseResultDetail.update_forward_refs()
GetEventPhaseResultDetailGetEventPhaseResultDetailDiscipline.update_forward_refs()
GetEventPhaseResultDetailGetEventPhaseResultDetailResult.update_forward_refs()
GetEventPhaseResultDetailGetEventPhaseResultDetailResultDiscipline.update_forward_refs()
