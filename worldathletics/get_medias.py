# Generated by ariadne-codegen on 2023-06-06 10:50
# Source: graphql/queries.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetMedias(BaseModel):
    get_medias: Optional[List[Optional["GetMediasGetMedias"]]] = Field(
        alias="getMedias"
    )


class GetMediasGetMedias(BaseModel):
    id: Optional[str]
    title: Optional[str]
    s_e_o_title: Optional[str] = Field(alias="sEOTitle")
    url_slug: Optional[str] = Field(alias="urlSlug")
    credit: Optional[str]
    show_in_media: Optional[bool] = Field(alias="showInMedia")
    complete: Optional[bool]
    file_name: Optional[str] = Field(alias="fileName")
    remote_item_code: Optional[str] = Field(alias="remoteItemCode")
    x_m_l_file_name360: Optional[str] = Field(alias="xMLFileName360")
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


GetMedias.update_forward_refs()
GetMediasGetMedias.update_forward_refs()
