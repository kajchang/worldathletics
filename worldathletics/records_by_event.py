# Generated by ariadne-codegen
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class RecordsByEvent(BaseModel):
    records_by_event: Optional[List[Optional["RecordsByEventRecordsByEvent"]]] = Field(
        alias="recordsByEvent"
    )


class RecordsByEventRecordsByEvent(BaseModel):
    progression_list_id: Optional[int] = Field(alias="progressionListId")
    category: Optional[str]
    performance: Optional[str]
    equal: Optional[bool]
    pending: Optional[bool]
    set_indoor: Optional[bool] = Field(alias="setIndoor")
    women_only: Optional[bool] = Field(alias="womenOnly")
    mixed: Optional[bool]
    yard: Optional[bool]
    wind: Optional[str]
    competitor: Optional["RecordsByEventRecordsByEventCompetitor"]
    country: Optional[str]
    venue: Optional[str]
    date: Optional[str]
    legend: Optional[str]
    discipline: Optional[str]
    discipline_name_url_slug: Optional[str] = Field(alias="disciplineNameUrlSlug")


class RecordsByEventRecordsByEventCompetitor(BaseModel):
    name: Optional[str]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    url_slug: Optional[str] = Field(alias="urlSlug")
    birth_date: Optional[str] = Field(alias="birthDate")


RecordsByEvent.model_rebuild()
RecordsByEventRecordsByEvent.model_rebuild()
