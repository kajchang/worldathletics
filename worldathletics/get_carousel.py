# Generated by ariadne-codegen
# Source: graphql/queries.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetCarousel(BaseModel):
    get_carousel: Optional["GetCarouselGetCarousel"] = Field(alias="getCarousel")


class GetCarouselGetCarousel(BaseModel):
    id: Optional[str]
    title: Optional[str]
    carousel_items: Optional[List[Optional["GetCarouselGetCarouselCarouselItems"]]] = (
        Field(alias="carouselItems")
    )
    media: Optional[List[Optional["GetCarouselGetCarouselMedia"]]]
    primary_media_ids: Optional[List[Optional[str]]] = Field(alias="primaryMediaIds")


class GetCarouselGetCarouselCarouselItems(BaseModel):
    id: Optional[str]
    title: Optional[str]
    description: Optional[str]
    description_second: Optional[str] = Field(alias="descriptionSecond")
    description_third: Optional[str] = Field(alias="descriptionThird")
    title_second: Optional[str] = Field(alias="titleSecond")
    title_third: Optional[str] = Field(alias="titleThird")
    title_fourth: Optional[str] = Field(alias="titleFourth")
    title_fifth: Optional[str] = Field(alias="titleFifth")
    title_direction: Optional[int] = Field(alias="titleDirection")
    home_carousel_id: Optional[str] = Field(alias="homeCarouselId")
    url: Optional[str]
    url_second: Optional[str] = Field(alias="urlSecond")
    url_third: Optional[str] = Field(alias="urlThird")
    url_fourth: Optional[str] = Field(alias="urlFourth")
    url_fifth: Optional[str] = Field(alias="urlFifth")
    primary_media_id: Optional[List[Optional[str]]] = Field(alias="primaryMediaId")
    primary_media: Optional[
        List[Optional["GetCarouselGetCarouselCarouselItemsPrimaryMedia"]]
    ] = Field(alias="primaryMedia")
    order: Optional[int]


class GetCarouselGetCarouselCarouselItemsPrimaryMedia(BaseModel):
    id: Optional[str]
    title: Optional[str]
    s_eo_title: Optional[str] = Field(alias="sEOTitle")
    url_slug: Optional[str] = Field(alias="urlSlug")
    credit: Optional[str]
    show_in_media: Optional[bool] = Field(alias="showInMedia")
    complete: Optional[bool]
    file_name: Optional[str] = Field(alias="fileName")
    remote_item_code: Optional[str] = Field(alias="remoteItemCode")
    x_ml_file_name_360: Optional[str] = Field(alias="xMLFileName360")
    file_name_url: Optional[str] = Field(alias="fileNameUrl")
    type: Optional[int]
    format: Optional[int]
    hosting: Optional[int]
    related_links: Optional[List[Optional[str]]] = Field(alias="relatedLinks")
    source_width: Optional[int] = Field(alias="sourceWidth")
    source_height: Optional[int] = Field(alias="sourceHeight")
    available_ratios: Optional[List[Optional[int]]] = Field(alias="availableRatios")
    related_sex_codes: Optional[List[Optional[int]]] = Field(alias="relatedSexCodes")
    related_age_groups: Optional[List[Optional[int]]] = Field(alias="relatedAgeGroups")
    related_event_phases: Optional[List[Optional[int]]] = Field(
        alias="relatedEventPhases"
    )
    status: Optional[int]
    live_from: Optional[Any] = Field(alias="liveFrom")
    created_on: Optional[str] = Field(alias="createdOn")
    updated_on: Optional[Any] = Field(alias="updatedOn")
    created_by_id: Optional[str] = Field(alias="createdById")
    updated_by_id: Optional[str] = Field(alias="updatedById")


class GetCarouselGetCarouselMedia(BaseModel):
    id: Optional[str]
    title: Optional[str]
    s_eo_title: Optional[str] = Field(alias="sEOTitle")
    url_slug: Optional[str] = Field(alias="urlSlug")
    credit: Optional[str]
    show_in_media: Optional[bool] = Field(alias="showInMedia")
    complete: Optional[bool]
    file_name: Optional[str] = Field(alias="fileName")
    remote_item_code: Optional[str] = Field(alias="remoteItemCode")
    x_ml_file_name_360: Optional[str] = Field(alias="xMLFileName360")
    file_name_url: Optional[str] = Field(alias="fileNameUrl")
    type: Optional[int]
    format: Optional[int]
    hosting: Optional[int]
    related_links: Optional[List[Optional[str]]] = Field(alias="relatedLinks")
    source_width: Optional[int] = Field(alias="sourceWidth")
    source_height: Optional[int] = Field(alias="sourceHeight")
    available_ratios: Optional[List[Optional[int]]] = Field(alias="availableRatios")
    related_sex_codes: Optional[List[Optional[int]]] = Field(alias="relatedSexCodes")
    related_age_groups: Optional[List[Optional[int]]] = Field(alias="relatedAgeGroups")
    related_event_phases: Optional[List[Optional[int]]] = Field(
        alias="relatedEventPhases"
    )
    status: Optional[int]
    live_from: Optional[Any] = Field(alias="liveFrom")
    created_on: Optional[str] = Field(alias="createdOn")
    updated_on: Optional[Any] = Field(alias="updatedOn")
    created_by_id: Optional[str] = Field(alias="createdById")
    updated_by_id: Optional[str] = Field(alias="updatedById")


GetCarousel.model_rebuild()
GetCarouselGetCarousel.model_rebuild()
GetCarouselGetCarouselCarouselItems.model_rebuild()
