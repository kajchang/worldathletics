# Generated by ariadne-codegen on 2023-06-06 10:50
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetWorldRankingsChanges(BaseModel):
    get_world_rankings_changes: Optional[
        "GetWorldRankingsChangesGetWorldRankingsChanges"
    ] = Field(alias="getWorldRankingsChanges")


class GetWorldRankingsChangesGetWorldRankingsChanges(BaseModel):
    module_title: Optional[str] = Field(alias="moduleTitle")
    module_subtitle: Optional[str] = Field(alias="moduleSubtitle")
    changes: Optional[
        List[Optional["GetWorldRankingsChangesGetWorldRankingsChangesChanges"]]
    ]


class GetWorldRankingsChangesGetWorldRankingsChangesChanges(BaseModel):
    ranking_calculation_id: Optional[int] = Field(alias="rankingCalculationId")
    place: Optional[int]
    previous_place: Optional[int] = Field(alias="previousPlace")
    improvement: Optional[str]
    event_name: Optional[str] = Field(alias="eventName")
    event_url_slug: Optional[str] = Field(alias="eventUrlSlug")
    score: Optional[int]
    competitor_id: Optional[int] = Field(alias="competitorId")
    competitor_name: Optional[str] = Field(alias="competitorName")
    sex_code: Optional[str] = Field(alias="sexCode")
    country_code: Optional[str] = Field(alias="countryCode")


GetWorldRankingsChanges.update_forward_refs()
GetWorldRankingsChangesGetWorldRankingsChanges.update_forward_refs()
GetWorldRankingsChangesGetWorldRankingsChangesChanges.update_forward_refs()
