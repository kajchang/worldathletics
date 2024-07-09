# Generated by ariadne-codegen on 2024-06-04 14:46
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetMedal(BaseModel):
    get_medal: Optional[List[Optional["GetMedalGetMedal"]]] = Field(alias="getMedal")


class GetMedalGetMedal(BaseModel):
    id: int
    event_id: int = Field(alias="eventId")
    country_code: Optional[str] = Field(alias="countryCode")
    country_name: Optional[str] = Field(alias="countryName")
    event_medal_table_order: Optional[int] = Field(alias="eventMedalTableOrder")
    event_sub_category_code: Optional[str] = Field(alias="eventSubCategoryCode")
    medal_rank: Optional[int] = Field(alias="medalRank")
    bronze: Optional[int]
    silver: Optional[int]
    gold: Optional[int]
    total: Optional[int]
    updated_on: Optional[str] = Field(alias="updatedOn")
    event_store_id: Optional[str] = Field(alias="eventStoreId")


GetMedal.update_forward_refs()
GetMedalGetMedal.update_forward_refs()
