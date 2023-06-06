# Generated by ariadne-codegen on 2023-06-06 10:49
# Source: graphql/queries.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetAssets(BaseModel):
    get_assets: Optional[List[Optional["GetAssetsGetAssets"]]] = Field(
        alias="getAssets"
    )


class GetAssetsGetAssets(BaseModel):
    id: Optional[str]
    slug: Optional[str]
    type_id: Optional[str] = Field(alias="typeId")
    thumbnail_feature_image_id: Optional[str] = Field(alias="thumbnailFeatureImageId")
    thumbnail_feature_image_edited: Optional[str] = Field(
        alias="thumbnailFeatureImageEdited"
    )
    thumbnail_feature_image: Optional[
        "GetAssetsGetAssetsThumbnailFeatureImage"
    ] = Field(alias="thumbnailFeatureImage")
    gated_content: Optional[bool] = Field(alias="gatedContent")
    download_only: Optional[bool] = Field(alias="downloadOnly")
    tags: Optional[List[Optional[str]]]
    published_by_name: Optional[str] = Field(alias="publishedByName")
    published: Optional[str]
    language: Optional[str]
    title: Optional[str]
    seo_description: Optional[str] = Field(alias="seoDescription")
    video: Optional[str]
    document_id: Optional[str] = Field(alias="documentId")
    document: Optional["GetAssetsGetAssetsDocument"]
    filters: Optional[List[Optional["GetAssetsGetAssetsFilters"]]]
    campaign_id: Optional[str] = Field(alias="campaignId")
    campaign: Optional["GetAssetsGetAssetsCampaign"]
    date: Optional[Any]


class GetAssetsGetAssetsThumbnailFeatureImage(BaseModel):
    id: Optional[str]
    media_type: Optional[str] = Field(alias="mediaType")
    title: Optional[str]
    copyright: Optional[str]
    file_name: Optional[str] = Field(alias="fileName")
    related_athletes: Optional[List[Optional[int]]] = Field(alias="relatedAthletes")
    related_disciplines: Optional[List[Optional[str]]] = Field(
        alias="relatedDisciplines"
    )
    related_competitions: Optional[List[Optional[str]]] = Field(
        alias="relatedCompetitions"
    )
    related_events: Optional[List[Optional[int]]] = Field(alias="relatedEvents")
    is_deleted: Optional[bool] = Field(alias="isDeleted")
    live_from: Optional[Any] = Field(alias="liveFrom")


class GetAssetsGetAssetsDocument(BaseModel):
    id: Optional[str]
    media_type: Optional[str] = Field(alias="mediaType")
    title: Optional[str]
    copyright: Optional[str]
    file_name: Optional[str] = Field(alias="fileName")
    related_athletes: Optional[List[Optional[int]]] = Field(alias="relatedAthletes")
    related_disciplines: Optional[List[Optional[str]]] = Field(
        alias="relatedDisciplines"
    )
    related_competitions: Optional[List[Optional[str]]] = Field(
        alias="relatedCompetitions"
    )
    related_events: Optional[List[Optional[int]]] = Field(alias="relatedEvents")
    is_deleted: Optional[bool] = Field(alias="isDeleted")
    live_from: Optional[Any] = Field(alias="liveFrom")


class GetAssetsGetAssetsFilters(BaseModel):
    id: Optional[str]
    content_id: Optional[str] = Field(alias="contentId")
    type_id: Optional[str] = Field(alias="typeId")
    type: Optional["GetAssetsGetAssetsFiltersType"]
    published: Optional[Any]
    published_by_id: Optional[str] = Field(alias="publishedById")
    published_by_name: Optional[str] = Field(alias="publishedByName")
    language: Optional[str]
    title: Optional[str]
    slug: Optional[str]


class GetAssetsGetAssetsFiltersType(BaseModel):
    id: Optional[str]
    content_id: Optional[str] = Field(alias="contentId")
    published: Optional[Any]
    published_by_id: Optional[str] = Field(alias="publishedById")
    published_by_name: Optional[str] = Field(alias="publishedByName")
    filters: Optional[List[Optional["GetAssetsGetAssetsFiltersTypeFilters"]]]
    language: Optional[str]
    title: Optional[str]
    slug: Optional[str]
    type_id: Optional[str] = Field(alias="typeId")
    site_id: Optional[str] = Field(alias="siteId")


class GetAssetsGetAssetsFiltersTypeFilters(BaseModel):
    id: Optional[str]
    content_id: Optional[str] = Field(alias="contentId")
    type_id: Optional[str] = Field(alias="typeId")
    published: Optional[Any]
    published_by_id: Optional[str] = Field(alias="publishedById")
    published_by_name: Optional[str] = Field(alias="publishedByName")
    language: Optional[str]
    title: Optional[str]
    slug: Optional[str]


class GetAssetsGetAssetsCampaign(BaseModel):
    id: Optional[str]
    name: Optional[str]
    tag: Optional[str]
    type: Optional[str]
    description: Optional[str]
    thank_you_message: Optional[str] = Field(alias="thankYouMessage")
    already_signed_message: Optional[str] = Field(alias="alreadySignedMessage")
    close_date: Optional[Any] = Field(alias="closeDate")
    redirect_url: Optional[str] = Field(alias="redirectUrl")
    tag_user_friendly_name: Optional[str] = Field(alias="tagUserFriendlyName")
    background_image_edited: Optional[str] = Field(alias="backgroundImageEdited")
    header_image_edited: Optional[str] = Field(alias="headerImageEdited")
    visible_on_preference_center: Optional[bool] = Field(
        alias="visibleOnPreferenceCenter"
    )
    short_form: Optional[bool] = Field(alias="shortForm")
    top_level_bucket_id: Optional[str] = Field(alias="topLevelBucketId")


GetAssets.update_forward_refs()
GetAssetsGetAssets.update_forward_refs()
GetAssetsGetAssetsThumbnailFeatureImage.update_forward_refs()
GetAssetsGetAssetsDocument.update_forward_refs()
GetAssetsGetAssetsFilters.update_forward_refs()
GetAssetsGetAssetsFiltersType.update_forward_refs()
GetAssetsGetAssetsFiltersTypeFilters.update_forward_refs()
GetAssetsGetAssetsCampaign.update_forward_refs()