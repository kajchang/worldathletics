# Generated by ariadne-codegen on 2023-06-06 10:49
# Source: graphql/queries.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetEventBrokenRecords(BaseModel):
    get_event_broken_records: Optional[
        List[Optional["GetEventBrokenRecordsGetEventBrokenRecords"]]
    ] = Field(alias="getEventBrokenRecords")


class GetEventBrokenRecordsGetEventBrokenRecords(BaseModel):
    id: Optional[int]
    phase_id: Optional[int] = Field(alias="phaseId")
    event_id: Optional[int] = Field(alias="eventId")
    record_order: Optional[int] = Field(alias="recordOrder")
    record_type_order: Optional[int] = Field(alias="recordTypeOrder")
    competitor_id__w_a: Optional[int] = Field(alias="competitorId_WA")
    record: Optional[str]
    sex_code: Optional[str] = Field(alias="sexCode")
    sex_name: Optional[str] = Field(alias="sexName")
    surname: Optional[str]
    forename: Optional[str]
    unit_name: Optional[str] = Field(alias="unitName")
    area_code: Optional[str] = Field(alias="areaCode")
    phase_name: Optional[str] = Field(alias="phaseName")
    phase_code: Optional[str] = Field(alias="phaseCode")
    sex_url_slug: Optional[str] = Field(alias="sexUrlSlug")
    result_rank: Optional[str] = Field(alias="resultRank")
    result_mark: Optional[str] = Field(alias="resultMark")
    record_name: Optional[str] = Field(alias="recordName")
    event_id__w_a: Optional[str] = Field(alias="eventId_WA")
    birth_date_str: Optional[str] = Field(alias="birthDateStr")
    unit_type_name: Optional[str] = Field(alias="unitTypeName")
    phase_url_slug: Optional[str] = Field(alias="phaseUrlSlug")
    competitor_id: Optional[str] = Field(alias="competitorId")
    discipline_code: Optional[str] = Field(alias="disciplineCode")
    discipline: Optional["GetEventBrokenRecordsGetEventBrokenRecordsDiscipline"]
    competitor_type_code: Optional[str] = Field(alias="competitorTypeCode")
    competitor_country_code: Optional[str] = Field(alias="competitorCountryCode")
    equalled: Optional[bool]
    updated_on: Optional[Any] = Field(alias="updatedOn")


class GetEventBrokenRecordsGetEventBrokenRecordsDiscipline(BaseModel):
    discipline_name: Optional[str] = Field(alias="disciplineName")
    discipline_code: Optional[str] = Field(alias="disciplineCode")
    type_name: Optional[str] = Field(alias="typeName")
    men: Optional[bool]
    women: Optional[bool]
    is_road: Optional[bool] = Field(alias="isRoad")
    is_walk: Optional[bool] = Field(alias="isWalk")
    is_wind: Optional[bool] = Field(alias="isWind")
    is_relay: Optional[bool] = Field(alias="isRelay")
    is_track: Optional[bool] = Field(alias="isTrack")
    is_field: Optional[bool] = Field(alias="isField")
    is_indoor: Optional[bool] = Field(alias="isIndoor")
    is_outdoor: Optional[bool] = Field(alias="isOutdoor")
    is_combined: Optional[bool] = Field(alias="isCombined")
    is_reaction: Optional[bool] = Field(alias="isReaction")
    is_valid_i_a_a_f: Optional[bool] = Field(alias="isValidIAAF")
    order: Optional[int]
    type_order: Optional[int] = Field(alias="typeOrder")
    id: Optional[str]
    name: Optional[str]
    hash: Optional[str]
    type_code: Optional[str] = Field(alias="typeCode")
    name_url_slug: Optional[str] = Field(alias="nameUrlSlug")
    type_name_url_slug: Optional[str] = Field(alias="typeNameUrlSlug")
    updated_on: Optional[Any] = Field(alias="updatedOn")


GetEventBrokenRecords.update_forward_refs()
GetEventBrokenRecordsGetEventBrokenRecords.update_forward_refs()
GetEventBrokenRecordsGetEventBrokenRecordsDiscipline.update_forward_refs()
