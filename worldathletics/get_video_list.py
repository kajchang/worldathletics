# Generated by ariadne-codegen on 2023-06-06 10:50
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetVideoList(BaseModel):
    get_video_list: Optional[List[Optional["GetVideoListGetVideoList"]]] = Field(
        alias="getVideoList"
    )


class GetVideoListGetVideoList(BaseModel):
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


GetVideoList.update_forward_refs()
GetVideoListGetVideoList.update_forward_refs()
