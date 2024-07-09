# Generated by ariadne-codegen on 2024-06-04 14:46
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetVideoById(BaseModel):
    get_video_by_id: Optional["GetVideoByIdGetVideoById"] = Field(alias="getVideoById")


class GetVideoByIdGetVideoById(BaseModel):
    id: Optional[str]
    content_id: Optional[str] = Field(alias="contentId")
    published_by_id: Optional[str] = Field(alias="publishedById")
    published_by_name: Optional[str] = Field(alias="publishedByName")
    published: Optional[str]
    language: Optional[str]
    gated_content: Optional[bool] = Field(alias="gatedContent")
    campaign_id: Optional[str] = Field(alias="campaignId")
    tags: Optional[List[Optional[str]]]
    title: Optional[str]
    thumbnail_id: Optional[str] = Field(alias="thumbnailId")
    thumbnail_edited: Optional[str] = Field(alias="thumbnailEdited")
    video_id: Optional[str] = Field(alias="videoId")
    player_id: Optional[str] = Field(alias="playerId")
    tag_id: Optional[str] = Field(alias="tagId")
    stand_first: Optional[str] = Field(alias="standFirst")
    signed_in_c_t_a: Optional[str] = Field(alias="signedInCTA")
    signed_out_c_t_a: Optional[str] = Field(alias="signedOutCTA")
    metatags: Optional[str]
    thumbnail_title: Optional[str] = Field(alias="thumbnailTitle")


GetVideoById.update_forward_refs()
GetVideoByIdGetVideoById.update_forward_refs()
