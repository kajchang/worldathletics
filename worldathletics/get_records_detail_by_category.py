# Generated by ariadne-codegen
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetRecordsDetailByCategory(BaseModel):
    get_records_detail_by_category: Optional[
        List[Optional["GetRecordsDetailByCategoryGetRecordsDetailByCategory"]]
    ] = Field(alias="getRecordsDetailByCategory")


class GetRecordsDetailByCategoryGetRecordsDetailByCategory(BaseModel):
    gender: Optional[str]
    results: Optional[
        List[Optional["GetRecordsDetailByCategoryGetRecordsDetailByCategoryResults"]]
    ]


class GetRecordsDetailByCategoryGetRecordsDetailByCategoryResults(BaseModel):
    progression_list_id: Optional[int] = Field(alias="progressionListId")
    discipline: Optional[str]
    discipline_name_url_slug: Optional[str] = Field(alias="disciplineNameUrlSlug")
    type_name_url_slug: Optional[str] = Field(alias="typeNameUrlSlug")
    performance: Optional[str]
    pending: Optional[bool]
    set_indoor: Optional[bool] = Field(alias="setIndoor")
    wind: Optional[str]
    competitor: Optional[
        "GetRecordsDetailByCategoryGetRecordsDetailByCategoryResultsCompetitor"
    ]
    venue: Optional[str]
    country: Optional[str]
    date: Optional[str]


class GetRecordsDetailByCategoryGetRecordsDetailByCategoryResultsCompetitor(BaseModel):
    id: Optional[int]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    name: Optional[str]
    country: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")
    birth_date: Optional[str] = Field(alias="birthDate")
    has_profile: Optional[bool] = Field(alias="hasProfile")
    team_members: Optional[
        List[
            Optional[
                "GetRecordsDetailByCategoryGetRecordsDetailByCategoryResultsCompetitorTeamMembers"
            ]
        ]
    ] = Field(alias="teamMembers")


class GetRecordsDetailByCategoryGetRecordsDetailByCategoryResultsCompetitorTeamMembers(
    BaseModel
):
    id: Optional[int]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    name: Optional[str]
    country: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")
    birth_date: Optional[str] = Field(alias="birthDate")
    has_profile: Optional[bool] = Field(alias="hasProfile")


GetRecordsDetailByCategory.model_rebuild()
GetRecordsDetailByCategoryGetRecordsDetailByCategory.model_rebuild()
GetRecordsDetailByCategoryGetRecordsDetailByCategoryResults.model_rebuild()
GetRecordsDetailByCategoryGetRecordsDetailByCategoryResultsCompetitor.model_rebuild()