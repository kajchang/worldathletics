# Generated by ariadne-codegen
# Source: graphql/queries.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetPlacingTable(BaseModel):
    get_placing_table: Optional[List[Optional["GetPlacingTableGetPlacingTable"]]] = (
        Field(alias="getPlacingTable")
    )


class GetPlacingTableGetPlacingTable(BaseModel):
    id: int
    event_id: int = Field(alias="eventId")
    rank: Optional[int]
    country_name: Optional[str] = Field(alias="countryName")
    country_code: Optional[str] = Field(alias="countryCode")
    gold: Optional[int]
    silver: Optional[int]
    bronze: Optional[int]
    forth: Optional[int]
    fifth: Optional[int]
    sixth: Optional[int]
    seventh: Optional[int]
    eighth: Optional[int]
    points: Optional[int]
    table_order: Optional[int] = Field(alias="tableOrder")
    sub_category_code: Optional[str] = Field(alias="subCategoryCode")
    updated_on: Optional[Any] = Field(alias="updatedOn")
    event_store_id: Optional[str] = Field(alias="eventStoreId")


GetPlacingTable.model_rebuild()
