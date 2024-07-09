# Generated by ariadne-codegen on 2024-06-04 14:46
# Source: graphql/schema.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class AAapiQuery(BaseModel):
    discipline_code: Optional[str] = Field(alias="disciplineCode")
    gender: Optional[str]
    environment: Optional[str]
    age_category: Optional[str] = Field(alias="ageCategory")
    wind_reading: Optional[str] = Field(alias="windReading")
    category_id: Optional[int] = Field(alias="categoryId")
    competition_id: Optional[int] = Field(alias="competitionId")
    event_group: Optional[str] = Field(alias="eventGroup")
    best_results_only: Optional[bool] = Field(alias="bestResultsOnly")
    region: Optional[str]
    region_type: Optional[str] = Field(alias="regionType")
    limit: Optional[int]
    season: Optional[int]
    page: Optional[int]
    max_year_available: Optional[int] = Field(alias="maxYearAvailable")


class ChunkType(BaseModel):
    size: Optional[int]
    chunk_order: Optional[int] = Field(alias="chunkOrder")
    chunk_id: Optional[str] = Field(alias="chunkId")


class ClientMetadataInput(BaseModel):
    key: Optional[str]
    value: Optional[str]


class CompetitorInput(BaseModel):
    competitor_id: Optional[int] = Field(alias="competitorId")
    old_competitor_id: Optional[int] = Field(alias="oldCompetitorId")
    first_name: Optional[str] = Field(alias="firstName")
    last_name: Optional[str] = Field(alias="lastName")
    birth_date: Optional[str] = Field(alias="birthDate")
    birth_place: Optional[str] = Field(alias="birthPlace")
    birth_country_code: Optional[str] = Field(alias="birthCountryCode")
    birth_place_country_name: Optional[str] = Field(alias="birthPlaceCountryName")
    team_name: Optional[str] = Field(alias="teamName")
    country_name: Optional[str] = Field(alias="countryName")
    country_code: Optional[str] = Field(alias="countryCode")
    sex_code: Optional[str] = Field(alias="sexCode")
    sex_name: Optional[str] = Field(alias="sexName")
    full_bio: Optional[str] = Field(alias="fullBio")
    butlers_bio: Optional[str] = Field(alias="butlersBio")


class CompetitorQueryInput(BaseModel):
    competitor_id: int = Field(alias="competitorId")


class EventInput(BaseModel):
    id: str
    timezone: Optional[str]
    updated_on: Optional[Any] = Field(alias="updatedOn")
    hash: Optional[str]
    name: Optional[str]
    start_date: Optional[Any] = Field(alias="startDate")
    end_date: Optional[Any] = Field(alias="endDate")
    venue: Optional[str]
    country_code: Optional[str] = Field(alias="countryCode")
    country_name: Optional[str] = Field(alias="countryName")
    area_code: Optional[str] = Field(alias="areaCode")
    area_name: Optional[str] = Field(alias="areaName")
    age_code: Optional[str] = Field(alias="ageCode")
    indoor_outdoor: Optional[str] = Field(alias="indoorOutdoor")
    category_code: Optional[str] = Field(alias="categoryCode")
    category_name: Optional[str] = Field(alias="categoryName")
    category_order: Optional[int] = Field(alias="categoryOrder")
    sub_category_code: Optional[str] = Field(alias="subCategoryCode")
    sub_category_name: Optional[str] = Field(alias="subCategoryName")
    sub_category_order: Optional[int] = Field(alias="subCategoryOrder")
    event_id__w_a: Optional[int] = Field(alias="eventId_WA")
    class_code: Optional[str] = Field(alias="classCode")
    class_name: Optional[str] = Field(alias="className")
    class_order: Optional[int] = Field(alias="classOrder")
    is_published: Optional[bool] = Field(alias="isPublished")
    has_comp_doc_results: Optional[bool] = Field(alias="hasCompDocResults")
    name_url_slug: Optional[str] = Field(alias="nameUrlSlug")
    start_date_year: Optional[int] = Field(alias="startDateYear")
    area_name_url_slug: Optional[str] = Field(alias="areaNameUrlSlug")
    category_name_url_slug: Optional[str] = Field(alias="categoryNameUrlSlug")
    sub_category_name_url_slug: Optional[str] = Field(alias="subCategoryNameUrlSlug")
    discipline_codes: Optional[List[Optional[str]]] = Field(alias="disciplineCodes")


class FlashInterviewInput(BaseModel):
    id: Optional[int]
    phase_id: Optional[int] = Field(alias="phaseId")
    phase_date: Optional[Any] = Field(alias="phaseDate")
    phase_name: Optional[str] = Field(alias="phaseName")
    unit_id: Optional[int] = Field(alias="unitId")
    unit_code: Optional[int] = Field(alias="unitCode")
    unit_type_name: Optional[str] = Field(alias="unitTypeName")
    unit_name: Optional[str] = Field(alias="unitName")
    title: Optional[str]
    body: Optional[str]
    competitor_id: Optional[int] = Field(alias="competitorId")
    competitor_team_name: Optional[str] = Field(alias="competitorTeamName")
    competitor_forename: Optional[str] = Field(alias="competitorForename")
    competitor_surname: Optional[str] = Field(alias="competitorSurname")
    competitor_country_code: Optional[str] = Field(alias="competitorCountryCode")
    competitor_sex: Optional[str] = Field(alias="competitorSex")
    competitor_type: Optional[str] = Field(alias="competitorType")
    updated_on: Optional[Any] = Field(alias="updatedOn")
    event_id: Optional[int] = Field(alias="eventId")
    discipline_code: Optional[str] = Field(alias="disciplineCode")
    discipline_name: Optional[str] = Field(alias="disciplineName")
    discipline_sex_name: Optional[str] = Field(alias="disciplineSexName")
    flash_interview_order: Optional[int] = Field(alias="flashInterviewOrder")
    flash_interview_date: Optional[Any] = Field(alias="flashInterviewDate")
    flash_interview_has_time: Optional[bool] = Field(alias="flashInterviewHasTime")
    event_store_id: Optional[str] = Field(alias="eventStoreId")


class LiveCombinedSummaryDetailInput(BaseModel):
    id: Optional[str]
    competition_id: Optional[int] = Field(alias="competitionId")
    phase_id: int = Field(alias="phaseId")
    overall_rank: Optional[int] = Field(alias="overallRank")
    bib: Optional[str]
    competitor_id: Optional[int] = Field(alias="competitorId")
    competitor_first_name: Optional[str] = Field(alias="competitorFirstName")
    competitor_last_name: Optional[str] = Field(alias="competitorLastName")
    competitor_country_code: Optional[str] = Field(alias="competitorCountryCode")
    competitor_birth_date: Optional[str] = Field(alias="competitorBirthDate")
    result_mark: Optional[str] = Field(alias="resultMark")
    record: Optional[str]
    details_disc_order: Optional[int] = Field(alias="detailsDiscOrder")
    discipline_code: Optional[str] = Field(alias="disciplineCode")
    discipline_mark: Optional[str] = Field(alias="disciplineMark")
    detail_wind: Optional[str] = Field(alias="detailWind")
    overall_points: Optional[int] = Field(alias="overallPoints")
    overall_order: Optional[int] = Field(alias="overallOrder")
    detail_combined_rank: Optional[str] = Field(alias="detailCombinedRank")
    discipline_rank: Optional[str] = Field(alias="disciplineRank")
    discipline_points: Optional[str] = Field(alias="disciplinePoints")
    update_on: Optional[str] = Field(alias="updateOn")
    combined_type: Optional[str] = Field(alias="combinedType")


class LivePhaseSummaryInput(BaseModel):
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
    competition_id: Optional[int] = Field(alias="competitionId")
    reaction_time: Optional[str] = Field(alias="reactionTime")
    phase_summary_milliseconds: Optional[str] = Field(alias="phaseSummaryMilliseconds")


class LivePhaseSummaryQuery(BaseModel):
    phase_id: Optional[int] = Field(alias="phaseId")


class LiveResultInput(BaseModel):
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
    team_members: Optional[List[Optional["LiveResultTeamMemberInput"]]] = Field(
        alias="teamMembers"
    )
    competition_id: Optional[int] = Field(alias="competitionId")
    result_milliseconds: Optional[str] = Field(alias="resultMilliseconds")
    world_ranking: Optional[str] = Field(alias="worldRanking")


class LiveResultTeamMemberInput(BaseModel):
    phase_id: Optional[int] = Field(alias="phaseId")
    unit_id: Optional[int] = Field(alias="unitId")
    unit_name: Optional[str] = Field(alias="unitName")
    live_result_id: Optional[int] = Field(alias="liveResultId")
    competitor_id: Optional[int] = Field(alias="competitorId")
    competitor_forename: Optional[str] = Field(alias="competitorForename")
    competitor_surname: Optional[str] = Field(alias="competitorSurname")
    competitor_country_name: Optional[str] = Field(alias="competitorCountryName")
    competitor_country_code: Optional[str] = Field(alias="competitorCountryCode")


class MedalDetailInput(BaseModel):
    id: Optional[int]
    medal_table_id: Optional[int] = Field(alias="medalTableId")
    type_id: Optional[int] = Field(alias="typeId")
    discipline_code: Optional[str] = Field(alias="disciplineCode")
    discipline_name: Optional[str] = Field(alias="disciplineName")
    sex_code: Optional[str] = Field(alias="sexCode")
    result_id: Optional[int] = Field(alias="resultId")
    result_mark: Optional[str] = Field(alias="resultMark")
    medal_date: Optional[str] = Field(alias="medalDate")
    details_order: Optional[int] = Field(alias="detailsOrder")
    competitor_id: Optional[int] = Field(alias="competitorId")
    competitor_first_name: Optional[str] = Field(alias="competitorFirstName")
    competitor_last_name: Optional[str] = Field(alias="competitorLastName")
    event_id: Optional[int] = Field(alias="eventId")
    phase_id: Optional[int] = Field(alias="phaseId")
    updated_on: Optional[str] = Field(alias="updatedOn")


class MedalInput(BaseModel):
    id: int
    event_id: int = Field(alias="eventId")
    country_code: Optional[str] = Field(alias="countryCode")
    country_name: Optional[str] = Field(alias="countryName")
    event_medal_table_order: Optional[int] = Field(alias="eventMedalTableOrder")
    event_sub_category_code: Optional[str] = Field(alias="eventSubCategoryCode")
    medal_rank: Optional[int] = Field(alias="medalRank")
    bronze: Optional[int]
    silver: Optional[int]
    gold: Optional[int]
    total: Optional[int]
    updated_on: Optional[str] = Field(alias="updatedOn")


class MedalMutationInput(BaseModel):
    event_id: int = Field(alias="eventId")
    payload: List["MedalInput"]


class PhaseInput(BaseModel):
    id: Optional[int]
    phase_code: Optional[str] = Field(alias="phaseCode")
    discipline_name: Optional[str] = Field(alias="disciplineName")
    discipline_order: Optional[int] = Field(alias="disciplineOrder")
    type_name: Optional[str] = Field(alias="typeName")
    type_code: Optional[str] = Field(alias="typeCode")
    type_order: Optional[int] = Field(alias="typeOrder")
    is_combined: Optional[bool] = Field(alias="isCombined")
    is_indoor: Optional[bool] = Field(alias="isIndoor")
    is_reaction: Optional[bool] = Field(alias="isReaction")
    is_outdoor: Optional[bool] = Field(alias="isOutdoor")
    is_wind: Optional[bool] = Field(alias="isWind")
    is_valid_i_a_a_f: Optional[bool] = Field(alias="isValidIAAF")
    is_relay: Optional[bool] = Field(alias="isRelay")
    is_walk: Optional[bool] = Field(alias="isWalk")
    is_road: Optional[bool] = Field(alias="isRoad")
    is_field: Optional[bool] = Field(alias="isField")
    is_track: Optional[bool] = Field(alias="isTrack")
    is_in_lane: Optional[bool] = Field(alias="isInLane")
    has_reaction_times: Optional[bool] = Field(alias="hasReactionTimes")
    has_wind_measurement: Optional[bool] = Field(alias="hasWindMeasurement")
    inout_code: Optional[bool] = Field(alias="inoutCode")
    has_team_standing: Optional[bool] = Field(alias="hasTeamStanding")
    disc_code_group: Optional[str] = Field(alias="discCodeGroup")
    phase_name: Optional[str] = Field(alias="phaseName")
    event_id: Optional[int] = Field(alias="eventId")
    event_id__w_a: Optional[int] = Field(alias="eventId_WA")
    phase_date_and_time: Optional[str] = Field(alias="phaseDateAndTime")
    sex_code: Optional[str] = Field(alias="sexCode")
    sex_name: Optional[str] = Field(alias="sexName")
    discipline_code: Optional[str] = Field(alias="disciplineCode")
    is_startlist_published: Optional[bool] = Field(alias="isStartlistPublished")
    is_result_published: Optional[bool] = Field(alias="isResultPublished")
    is_phase_summary_published: Optional[bool] = Field(alias="isPhaseSummaryPublished")
    is_team_standing_published: Optional[bool] = Field(alias="isTeamStandingPublished")
    combined_discipline_order: Optional[str] = Field(alias="combinedDisciplineOrder")
    phase_order: Optional[int] = Field(alias="phaseOrder")
    phase_session_order: Optional[int] = Field(alias="phaseSessionOrder")
    phase_session_name: Optional[str] = Field(alias="phaseSessionName")
    primary_phase_order: Optional[int] = Field(alias="primaryPhaseOrder")
    status: Optional[int]
    has_time: Optional[int] = Field(alias="hasTime")
    updated_on: Optional[str] = Field(alias="updatedOn")
    units: List["UnitInput"]


class PhaseQueryInput(BaseModel):
    competition_id: int = Field(alias="competitionId")
    sex_code: Optional[str] = Field(alias="sexCode")
    discipline_code: Optional[str] = Field(alias="disciplineCode")


class PlacingTableDetailInput(BaseModel):
    id: int
    placing_table_id: int = Field(alias="placingTableId")
    competitor_id: Optional[int] = Field(alias="competitorId")
    discipline_code: Optional[str] = Field(alias="disciplineCode")
    discipline_name: Optional[str] = Field(alias="disciplineName")
    competitor_first_name: Optional[str] = Field(alias="competitorFirstName")
    competitor_last_name: Optional[str] = Field(alias="competitorLastName")
    sex_code: Optional[str] = Field(alias="sexCode")
    placing_date: Optional[Any] = Field(alias="placingDate")
    details_order: Optional[int] = Field(alias="detailsOrder")
    event_id: Optional[int] = Field(alias="eventId")
    type_id: Optional[int] = Field(alias="typeId")
    type_name: Optional[str] = Field(alias="typeName")
    type_abbreviation: Optional[str] = Field(alias="typeAbbreviation")
    result_mark: Optional[str] = Field(alias="resultMark")
    placing_points: Optional[str] = Field(alias="placingPoints")
    result_id: Optional[int] = Field(alias="resultId")
    phase_id: Optional[int] = Field(alias="phaseId")
    country_code: Optional[str] = Field(alias="countryCode")
    updated_on: Optional[Any] = Field(alias="updatedOn")


class PlacingTableInput(BaseModel):
    id: int
    event_id: int = Field(alias="eventId")
    rank: Optional[int]
    country_name: Optional[str] = Field(alias="countryName")
    country_code: Optional[str] = Field(alias="countryCode")
    gold: Optional[int]
    silver: Optional[int]
    bronze: Optional[int]
    forth: Optional[int]
    fifth: Optional[int]
    sixth: Optional[int]
    seventh: Optional[int]
    eighth: Optional[int]
    points: Optional[int]
    table_order: Optional[int] = Field(alias="tableOrder")
    sub_category_code: Optional[str] = Field(alias="subCategoryCode")
    updated_on: Optional[Any] = Field(alias="updatedOn")


class PreviousMedalQuery(BaseModel):
    event_id: Optional[int] = Field(alias="eventId")
    event_id__w_a: Optional[int] = Field(alias="eventId_WA")
    event_end_date: Optional[str] = Field(alias="eventEndDate")
    sub_category_code: Optional[str] = Field(alias="subCategoryCode")
    gender: Optional[str]
    discipline_code: Optional[str] = Field(alias="disciplineCode")
    indoor_out_door: Optional[str] = Field(alias="indoorOutDoor")


class TeamQuery(BaseModel):
    team_id: Optional[int] = Field(alias="teamId")
    team_sex: Optional[str] = Field(alias="teamSex")
    indoor_outdoor: Optional[str] = Field(alias="indoorOutdoor")


class TeamScoringInput(BaseModel):
    id: str
    team_id: Optional[int] = Field(alias="teamId")
    team_id__w_a: Optional[int] = Field(alias="teamId_WA")
    phase_id: Optional[int] = Field(alias="phaseId")
    unit_id: Optional[int] = Field(alias="unitId")
    scoring_team_id: Optional[int] = Field(alias="scoringTeamId")
    result_id: Optional[int] = Field(alias="resultId")
    old_competitor_id: Optional[int] = Field(alias="oldCompetitorId")
    competitor_id: Optional[int] = Field(alias="competitorId")
    competitor_id__w_a: Optional[int] = Field(alias="competitorId_WA")
    team_name: Optional[str] = Field(alias="teamName")
    team_country_code: Optional[str] = Field(alias="teamCountryCode")
    updated_on: Optional[Any] = Field(alias="updatedOn")
    scoring_team_order: Optional[int] = Field(alias="scoringTeamOrder")
    scoring_team_detail_order: Optional[int] = Field(alias="scoringTeamDetailOrder")
    bib: Optional[str]
    event_store_id: Optional[str] = Field(alias="eventStoreId")
    chunk_order: Optional[int] = Field(alias="chunkOrder")
    chunk_id: Optional[str] = Field(alias="chunkId")


class TeamStandingsInput(BaseModel):
    id: Optional[int]
    phase_id: Optional[int] = Field(alias="phaseId")
    unit_id: Optional[int] = Field(alias="unitId")
    competition_intermediate_id: Optional[int] = Field(
        alias="competitionIntermediateId"
    )
    competition_intermediate_name: Optional[str] = Field(
        alias="competitionIntermediateName"
    )
    rank: Optional[int]
    team_id: Optional[int] = Field(alias="teamId")
    team_id__w_a: Optional[int] = Field(alias="teamId_WA")
    team_name: Optional[str] = Field(alias="teamName")
    team_country_code: Optional[str] = Field(alias="teamCountryCode")
    standing_mark: Optional[str] = Field(alias="standingMark")
    live_current: Optional[bool] = Field(alias="liveCurrent")
    updated_on: Optional[Any] = Field(alias="updatedOn")
    team_standing_id: Optional[int] = Field(alias="teamStandingId")
    competition_intermediate_order: Optional[int] = Field(
        alias="competitionIntermediateOrder"
    )
    detail_rank: Optional[int] = Field(alias="detailRank")
    standing_detail_bib: Optional[str] = Field(alias="standingDetailBib")
    competitor_id: Optional[int] = Field(alias="competitorId")
    competitor_id__w_a: Optional[int] = Field(alias="competitorId_WA")
    old_competitor_id: Optional[int] = Field(alias="oldCompetitorId")
    standing_detail_score: Optional[str] = Field(alias="standingDetailScore")
    standing_detail_scoring: Optional[str] = Field(alias="standingDetailScoring")
    team_standing_order: Optional[int] = Field(alias="teamStandingOrder")
    team_standing_detail_order: Optional[int] = Field(alias="teamStandingDetailOrder")
    chunk_order: Optional[int] = Field(alias="chunkOrder")
    chunk_id: Optional[str] = Field(alias="chunkId")


class UnitInput(BaseModel):
    id: Optional[int]
    phase_id: Optional[int] = Field(alias="phaseId")
    unit_name: Optional[str] = Field(alias="unitName")
    unit_type: Optional[str] = Field(alias="unitType")
    unit_order: Optional[int] = Field(alias="unitOrder")
    is_startlist_published: Optional[bool] = Field(alias="isStartlistPublished")
    is_result_published: Optional[bool] = Field(alias="isResultPublished")
    is_phase_summary_published: Optional[bool] = Field(alias="isPhaseSummaryPublished")
    is_team_standing_published: Optional[bool] = Field(alias="isTeamStandingPublished")
    combined_discipline_order: Optional[str] = Field(alias="combinedDisciplineOrder")
    status: Optional[str]
    qualification_rule_code: Optional[str] = Field(alias="qualificationRuleCode")
    updated_on: Optional[str] = Field(alias="updatedOn")
    start_date: Optional[str] = Field(alias="startDate")
    start_time: Optional[str] = Field(alias="startTime")
    start_date_time: Optional[str] = Field(alias="startDateTime")
    wind: Optional[str]


AAapiQuery.update_forward_refs()
ChunkType.update_forward_refs()
ClientMetadataInput.update_forward_refs()
CompetitorInput.update_forward_refs()
CompetitorQueryInput.update_forward_refs()
EventInput.update_forward_refs()
FlashInterviewInput.update_forward_refs()
LiveCombinedSummaryDetailInput.update_forward_refs()
LivePhaseSummaryInput.update_forward_refs()
LivePhaseSummaryQuery.update_forward_refs()
LiveResultInput.update_forward_refs()
LiveResultTeamMemberInput.update_forward_refs()
MedalDetailInput.update_forward_refs()
MedalInput.update_forward_refs()
MedalMutationInput.update_forward_refs()
PhaseInput.update_forward_refs()
PhaseQueryInput.update_forward_refs()
PlacingTableDetailInput.update_forward_refs()
PlacingTableInput.update_forward_refs()
PreviousMedalQuery.update_forward_refs()
TeamQuery.update_forward_refs()
TeamScoringInput.update_forward_refs()
TeamStandingsInput.update_forward_refs()
UnitInput.update_forward_refs()
