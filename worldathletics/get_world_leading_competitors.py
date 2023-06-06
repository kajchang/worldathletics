# Generated by ariadne-codegen on 2023-06-06 10:50
# Source: graphql/queries.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetWorldLeadingCompetitors(BaseModel):
    get_world_leading_competitors: Optional[
        "GetWorldLeadingCompetitorsGetWorldLeadingCompetitors"
    ] = Field(alias="getWorldLeadingCompetitors")


class GetWorldLeadingCompetitorsGetWorldLeadingCompetitors(BaseModel):
    module_title: Optional[str] = Field(alias="moduleTitle")
    module_subtitle: Optional[str] = Field(alias="moduleSubtitle")
    event_results: Optional[
        List[
            Optional["GetWorldLeadingCompetitorsGetWorldLeadingCompetitorsEventResults"]
        ]
    ] = Field(alias="eventResults")


class GetWorldLeadingCompetitorsGetWorldLeadingCompetitorsEventResults(BaseModel):
    event_name: Optional[str] = Field(alias="eventName")
    environment: Optional[str]
    age_category: Optional[str] = Field(alias="ageCategory")
    season: Optional[int]
    discipline_url_slug: Optional[str] = Field(alias="disciplineUrlSlug")
    discipline_type_url_slug: Optional[str] = Field(alias="disciplineTypeUrlSlug")
    sex_code: Optional[str] = Field(alias="sexCode")
    results: Optional[
        List[
            Optional[
                "GetWorldLeadingCompetitorsGetWorldLeadingCompetitorsEventResultsResults"
            ]
        ]
    ]


class GetWorldLeadingCompetitorsGetWorldLeadingCompetitorsEventResultsResults(
    BaseModel
):
    mark: Optional[str]
    country_code: Optional[str] = Field(alias="countryCode")
    competitor: Optional[
        "GetWorldLeadingCompetitorsGetWorldLeadingCompetitorsEventResultsResultsCompetitor"
    ]
    primary_media_id: Optional[List[Optional[str]]] = Field(alias="primaryMediaId")
    primary_media: Optional[
        List[
            Optional[
                "GetWorldLeadingCompetitorsGetWorldLeadingCompetitorsEventResultsResultsPrimaryMedia"
            ]
        ]
    ] = Field(alias="primaryMedia")


class GetWorldLeadingCompetitorsGetWorldLeadingCompetitorsEventResultsResultsCompetitor(
    BaseModel
):
    name: Optional[str]
    id: Optional[int]
    url_slug: Optional[str] = Field(alias="urlSlug")
    country_url_slug: Optional[str] = Field(alias="countryUrlSlug")
    birth_date: Optional[Any] = Field(alias="birthDate")


class GetWorldLeadingCompetitorsGetWorldLeadingCompetitorsEventResultsResultsPrimaryMedia(
    BaseModel
):
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


GetWorldLeadingCompetitors.update_forward_refs()
GetWorldLeadingCompetitorsGetWorldLeadingCompetitors.update_forward_refs()
GetWorldLeadingCompetitorsGetWorldLeadingCompetitorsEventResults.update_forward_refs()
GetWorldLeadingCompetitorsGetWorldLeadingCompetitorsEventResultsResults.update_forward_refs()
GetWorldLeadingCompetitorsGetWorldLeadingCompetitorsEventResultsResultsCompetitor.update_forward_refs()
GetWorldLeadingCompetitorsGetWorldLeadingCompetitorsEventResultsResultsPrimaryMedia.update_forward_refs()