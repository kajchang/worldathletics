# Generated by ariadne-codegen
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetRecordsDisciplineList(BaseModel):
    get_records_discipline_list: Optional[
        List[Optional["GetRecordsDisciplineListGetRecordsDisciplineList"]]
    ] = Field(alias="getRecordsDisciplineList")


class GetRecordsDisciplineListGetRecordsDisciplineList(BaseModel):
    gender: Optional[str]
    discipline_types: Optional[
        List[
            Optional["GetRecordsDisciplineListGetRecordsDisciplineListDisciplineTypes"]
        ]
    ] = Field(alias="disciplineTypes")


class GetRecordsDisciplineListGetRecordsDisciplineListDisciplineTypes(BaseModel):
    name: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")
    disciplines: Optional[
        List[
            Optional[
                "GetRecordsDisciplineListGetRecordsDisciplineListDisciplineTypesDisciplines"
            ]
        ]
    ]


class GetRecordsDisciplineListGetRecordsDisciplineListDisciplineTypesDisciplines(
    BaseModel
):
    event_id: Optional[str] = Field(alias="eventId")
    name: Optional[str]
    url_slug: Optional[str] = Field(alias="urlSlug")


GetRecordsDisciplineList.model_rebuild()
GetRecordsDisciplineListGetRecordsDisciplineList.model_rebuild()
GetRecordsDisciplineListGetRecordsDisciplineListDisciplineTypes.model_rebuild()
