# Generated by ariadne-codegen
# Source: graphql/queries.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetLeadingAthletes(BaseModel):
    get_leading_athletes: Optional["GetLeadingAthletesGetLeadingAthletes"] = Field(
        alias="getLeadingAthletes"
    )


class GetLeadingAthletesGetLeadingAthletes(BaseModel):
    event_results: Optional[
        List[Optional["GetLeadingAthletesGetLeadingAthletesEventResults"]]
    ] = Field(alias="eventResults")


class GetLeadingAthletesGetLeadingAthletesEventResults(BaseModel):
    event_name: Optional[str] = Field(alias="eventName")
    environment: Optional[str]
    age_category: Optional[str] = Field(alias="ageCategory")
    season: Optional[int]
    discipline_url_slug: Optional[str] = Field(alias="disciplineUrlSlug")
    discipline_type_url_slug: Optional[str] = Field(alias="disciplineTypeUrlSlug")
    sex_code: Optional[str] = Field(alias="sexCode")
    results: Optional[
        List[Optional["GetLeadingAthletesGetLeadingAthletesEventResultsResults"]]
    ]


class GetLeadingAthletesGetLeadingAthletesEventResultsResults(BaseModel):
    mark: Optional[str]
    country_code: Optional[str] = Field(alias="countryCode")
    competitor: Optional[
        "GetLeadingAthletesGetLeadingAthletesEventResultsResultsCompetitor"
    ]
    primary_media_id: Optional[List[Optional[str]]] = Field(alias="primaryMediaId")
    primary_media: Optional[
        List[
            Optional[
                "GetLeadingAthletesGetLeadingAthletesEventResultsResultsPrimaryMedia"
            ]
        ]
    ] = Field(alias="primaryMedia")


class GetLeadingAthletesGetLeadingAthletesEventResultsResultsCompetitor(BaseModel):
    name: Optional[str]
    id: Optional[int]
    url_slug: Optional[str] = Field(alias="urlSlug")
    country_url_slug: Optional[str] = Field(alias="countryUrlSlug")
    birth_date: Optional[Any] = Field(alias="birthDate")
    team_members: Optional[
        List[
            Optional[
                "GetLeadingAthletesGetLeadingAthletesEventResultsResultsCompetitorTeamMembers"
            ]
        ]
    ] = Field(alias="teamMembers")


class GetLeadingAthletesGetLeadingAthletesEventResultsResultsCompetitorTeamMembers(
    BaseModel
):
    id: Optional[int]
    name: Optional[str]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    url_slug: Optional[str] = Field(alias="urlSlug")


class GetLeadingAthletesGetLeadingAthletesEventResultsResultsPrimaryMedia(BaseModel):
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


GetLeadingAthletes.model_rebuild()
GetLeadingAthletesGetLeadingAthletes.model_rebuild()
GetLeadingAthletesGetLeadingAthletesEventResults.model_rebuild()
GetLeadingAthletesGetLeadingAthletesEventResultsResults.model_rebuild()
GetLeadingAthletesGetLeadingAthletesEventResultsResultsCompetitor.model_rebuild()
