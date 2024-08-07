# Generated by ariadne-codegen
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetWorldRanking(BaseModel):
    get_world_ranking: Optional[List[Optional["GetWorldRankingGetWorldRanking"]]] = (
        Field(alias="getWorldRanking")
    )


class GetWorldRankingGetWorldRanking(BaseModel):
    id: Optional[int]
    place: Optional[int]
    world_place: Optional[int] = Field(alias="worldPlace")
    athlete: Optional[str]
    athlete_url_slug: Optional[str] = Field(alias="athleteUrlSlug")
    birth_date: Optional[str] = Field(alias="birthDate")
    nationality: Optional[str]
    ranking_score: Optional[int] = Field(alias="rankingScore")
    disciplines: Optional[str]
    country_place: Optional[int] = Field(alias="countryPlace")
    previous_id: Optional[int] = Field(alias="previousId")
    previous_place: Optional[int] = Field(alias="previousPlace")
    previous_ranking_score: Optional[int] = Field(alias="previousRankingScore")


GetWorldRanking.model_rebuild()
