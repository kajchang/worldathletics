# Generated by ariadne-codegen on 2023-06-06 10:49
# Source: graphql/queries.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetAssetsDates(BaseModel):
    get_assets_dates: Optional["GetAssetsDatesGetAssetsDates"] = Field(
        alias="getAssetsDates"
    )


class GetAssetsDatesGetAssetsDates(BaseModel):
    dates: Optional[List[Optional[Any]]]


GetAssetsDates.update_forward_refs()
GetAssetsDatesGetAssetsDates.update_forward_refs()
