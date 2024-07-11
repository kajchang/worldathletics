# Generated by ariadne-codegen
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetRecordsDetailByProgression(BaseModel):
    get_records_detail_by_progression: Optional[
        "GetRecordsDetailByProgressionGetRecordsDetailByProgression"
    ] = Field(alias="getRecordsDetailByProgression")


class GetRecordsDetailByProgressionGetRecordsDetailByProgression(BaseModel):
    age_category: Optional[str] = Field(alias="ageCategory")
    environment: Optional[str]
    gender: Optional[str]
    discipline: Optional[
        "GetRecordsDetailByProgressionGetRecordsDetailByProgressionDiscipline"
    ]
    origin_type: Optional[str] = Field(alias="originType")
    origin: Optional[str]
    entries: Optional[
        List[
            Optional[
                "GetRecordsDetailByProgressionGetRecordsDetailByProgressionEntries"
            ]
        ]
    ]


class GetRecordsDetailByProgressionGetRecordsDetailByProgressionDiscipline(BaseModel):
    name: Optional[str]
    discipline_code: Optional[str] = Field(alias="disciplineCode")
    url_slug: Optional[str] = Field(alias="urlSlug")


class GetRecordsDetailByProgressionGetRecordsDetailByProgressionEntries(BaseModel):
    progression_list_id: Optional[int] = Field(alias="progressionListId")
    category: Optional[str]
    category_id: Optional[int] = Field(alias="categoryId")
    performance: Optional[str]
    equal: Optional[bool]
    pending: Optional[bool]
    set_indoor: Optional[bool] = Field(alias="setIndoor")
    women_only: Optional[bool] = Field(alias="womenOnly")
    mixed: Optional[bool]
    yard: Optional[bool]
    wind: Optional[str]
    competitor: Optional[
        "GetRecordsDetailByProgressionGetRecordsDetailByProgressionEntriesCompetitor"
    ]
    country: Optional[str]
    venue: Optional[str]
    date: Optional[str]


class GetRecordsDetailByProgressionGetRecordsDetailByProgressionEntriesCompetitor(
    BaseModel
):
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
                "GetRecordsDetailByProgressionGetRecordsDetailByProgressionEntriesCompetitorTeamMembers"
            ]
        ]
    ] = Field(alias="teamMembers")


class GetRecordsDetailByProgressionGetRecordsDetailByProgressionEntriesCompetitorTeamMembers(
    BaseModel
):
    id: Optional[int]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    name: Optional[str]
    country: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")
    birth_date: Optional[str] = Field(alias="birthDate")
    has_profile: Optional[bool] = Field(alias="hasProfile")


GetRecordsDetailByProgression.model_rebuild()
GetRecordsDetailByProgressionGetRecordsDetailByProgression.model_rebuild()
GetRecordsDetailByProgressionGetRecordsDetailByProgressionEntries.model_rebuild()
GetRecordsDetailByProgressionGetRecordsDetailByProgressionEntriesCompetitor.model_rebuild()