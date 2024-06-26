# Generated by ariadne-codegen on 2024-06-04 13:40
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetTopList(BaseModel):
    get_top_list: Optional["GetTopListGetTopList"] = Field(alias="getTopList")


class GetTopListGetTopList(BaseModel):
    page: Optional[int]
    pages: Optional[int]
    payload: Optional[List[Optional["GetTopListGetTopListPayload"]]]


class GetTopListGetTopListPayload(BaseModel):
    position: Optional[int]
    place: Optional[str]
    achiever_position: Optional[int] = Field(alias="achieverPosition")
    result: Optional[str]
    achiever: Optional[str]
    nationality: Optional[str]
    venue: Optional[str]
    date: Optional[str]
    result_score: Optional[int] = Field(alias="resultScore")


GetTopList.update_forward_refs()
GetTopListGetTopList.update_forward_refs()
GetTopListGetTopListPayload.update_forward_refs()
