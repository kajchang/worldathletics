# Generated by ariadne-codegen
# Source: graphql/queries.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetTeamScoring(BaseModel):
    get_team_scoring: Optional[List[Optional["GetTeamScoringGetTeamScoring"]]] = Field(
        alias="getTeamScoring"
    )


class GetTeamScoringGetTeamScoring(BaseModel):
    id: str
    team_id: Optional[int] = Field(alias="teamId")
    team_id_wa: Optional[int] = Field(alias="teamId_WA")
    phase_id: Optional[int] = Field(alias="phaseId")
    unit_id: Optional[int] = Field(alias="unitId")
    result_id: Optional[int] = Field(alias="resultId")
    team_name: Optional[str] = Field(alias="teamName")
    team_country_code: Optional[str] = Field(alias="teamCountryCode")
    competitor_id: Optional[List[Optional[int]]] = Field(alias="competitorId")
    athlete: Optional[List[Optional["GetTeamScoringGetTeamScoringAthlete"]]]
    updated_on: Optional[Any] = Field(alias="updatedOn")
    scoring_team_id: Optional[int] = Field(alias="scoringTeamId")
    scoring_team_order: Optional[int] = Field(alias="scoringTeamOrder")
    scoring_team_detail_order: Optional[int] = Field(alias="scoringTeamDetailOrder")
    bib: Optional[str]
    event_store_id: Optional[str] = Field(alias="eventStoreId")
    chunk_order: Optional[int] = Field(alias="chunkOrder")
    chunk_id: Optional[str] = Field(alias="chunkId")


class GetTeamScoringGetTeamScoringAthlete(BaseModel):
    competitor_id: Optional[List[Optional[int]]] = Field(alias="competitorId")
    detail: Optional[List[Optional["GetTeamScoringGetTeamScoringAthleteDetail"]]]
    first_name: Optional[str] = Field(alias="firstName")
    last_name: Optional[str] = Field(alias="lastName")
    birth_date: Optional[Any] = Field(alias="birthDate")
    birth_place: Optional[str] = Field(alias="birthPlace")
    birth_country_code: Optional[str] = Field(alias="birthCountryCode")
    birth_place_country_name: Optional[str] = Field(alias="birthPlaceCountryName")
    team_name: Optional[str] = Field(alias="teamName")
    country_name: Optional[str] = Field(alias="countryName")
    country_code: Optional[str] = Field(alias="countryCode")
    sex_code: Optional[str] = Field(alias="sexCode")
    sex_name: Optional[str] = Field(alias="sexName")


class GetTeamScoringGetTeamScoringAthleteDetail(BaseModel):
    id: Optional[int]
    updated_on: Optional[Any] = Field(alias="updatedOn")
    hash: Optional[str]
    type_code: Optional[str] = Field(alias="typeCode")
    first_name: Optional[str] = Field(alias="firstName")
    last_name: Optional[str] = Field(alias="lastName")
    sex_code: Optional[str] = Field(alias="sexCode")
    sex_name: Optional[str] = Field(alias="sexName")
    country_code: Optional[str] = Field(alias="countryCode")
    country_name: Optional[str] = Field(alias="countryName")
    birth_date_str: Optional[str] = Field(alias="birthDateStr")
    url_slug: Optional[str] = Field(alias="urlSlug")
    representative_id: Optional[int] = Field(alias="representativeId")
    name: Optional[str]
    country_url_slug: Optional[str] = Field(alias="countryUrlSlug")
    sex_name_url_slug: Optional[str] = Field(alias="sexNameUrlSlug")
    friendly_name: Optional[str] = Field(alias="friendlyName")
    friendly_name_letter: Optional[str] = Field(alias="friendlyNameLetter")
    friendly_name_first_3_letter: Optional[str] = Field(
        alias="friendlyNameFirst3Letter"
    )


GetTeamScoring.model_rebuild()
GetTeamScoringGetTeamScoring.model_rebuild()
GetTeamScoringGetTeamScoringAthlete.model_rebuild()
