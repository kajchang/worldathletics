# Generated by ariadne-codegen on 2024-06-04 14:46
# Source: graphql/queries.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetWorldRankings(BaseModel):
    get_world_rankings: Optional["GetWorldRankingsGetWorldRankings"] = Field(
        alias="getWorldRankings"
    )


class GetWorldRankingsGetWorldRankings(BaseModel):
    parameters: Optional["GetWorldRankingsGetWorldRankingsParameters"]
    rank_date: Optional[str] = Field(alias="rankDate")
    event_group: Optional[str] = Field(alias="eventGroup")
    rankings: Optional[List[Optional["GetWorldRankingsGetWorldRankingsRankings"]]]


class GetWorldRankingsGetWorldRankingsParameters(BaseModel):
    rank_date: Optional[Any] = Field(alias="rankDate")
    gender: Optional[str]
    event_group: Optional[str] = Field(alias="eventGroup")
    region_type: Optional[str] = Field(alias="regionType")
    limited_by_country: Optional[int] = Field(alias="limitedByCountry")
    limit: Optional[int]


class GetWorldRankingsGetWorldRankingsRankings(BaseModel):
    id: int
    place: Optional[int]
    competitor_name: Optional[str] = Field(alias="competitorName")
    competitor_country_url_slug: Optional[str] = Field(alias="competitorCountryUrlSlug")
    competitor_url_slug: Optional[str] = Field(alias="competitorUrlSlug")
    competitor_birth_date: Optional[Any] = Field(alias="competitorBirthDate")
    country_code: Optional[str] = Field(alias="countryCode")
    ranking_score: Optional[int] = Field(alias="rankingScore")
    discipline_codes: Optional[List[Optional[str]]] = Field(alias="disciplineCodes")
    country_place: Optional[int] = Field(alias="countryPlace")
    previous_id: Optional[int] = Field(alias="previousId")
    previous_place: Optional[int] = Field(alias="previousPlace")
    previous_ranking_score: Optional[int] = Field(alias="previousRankingScore")


GetWorldRankings.update_forward_refs()
GetWorldRankingsGetWorldRankings.update_forward_refs()
GetWorldRankingsGetWorldRankingsParameters.update_forward_refs()
GetWorldRankingsGetWorldRankingsRankings.update_forward_refs()
