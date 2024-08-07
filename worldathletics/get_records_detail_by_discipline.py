# Generated by ariadne-codegen
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetRecordsDetailByDiscipline(BaseModel):
    get_records_detail_by_discipline: Optional[
        List[Optional["GetRecordsDetailByDisciplineGetRecordsDetailByDiscipline"]]
    ] = Field(alias="getRecordsDetailByDiscipline")


class GetRecordsDetailByDisciplineGetRecordsDetailByDiscipline(BaseModel):
    age_category: Optional[str] = Field(alias="ageCategory")
    items: Optional[
        List[Optional["GetRecordsDetailByDisciplineGetRecordsDetailByDisciplineItems"]]
    ]


class GetRecordsDetailByDisciplineGetRecordsDetailByDisciplineItems(BaseModel):
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
        "GetRecordsDetailByDisciplineGetRecordsDetailByDisciplineItemsCompetitor"
    ]
    country: Optional[str]
    venue: Optional[str]
    date: Optional[str]


class GetRecordsDetailByDisciplineGetRecordsDetailByDisciplineItemsCompetitor(
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
                "GetRecordsDetailByDisciplineGetRecordsDetailByDisciplineItemsCompetitorTeamMembers"
            ]
        ]
    ] = Field(alias="teamMembers")


class GetRecordsDetailByDisciplineGetRecordsDetailByDisciplineItemsCompetitorTeamMembers(
    BaseModel
):
    id: Optional[int]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    name: Optional[str]
    country: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")
    birth_date: Optional[str] = Field(alias="birthDate")
    has_profile: Optional[bool] = Field(alias="hasProfile")


GetRecordsDetailByDiscipline.model_rebuild()
GetRecordsDetailByDisciplineGetRecordsDetailByDiscipline.model_rebuild()
GetRecordsDetailByDisciplineGetRecordsDetailByDisciplineItems.model_rebuild()
GetRecordsDetailByDisciplineGetRecordsDetailByDisciplineItemsCompetitor.model_rebuild()
