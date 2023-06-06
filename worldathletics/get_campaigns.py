# Generated by ariadne-codegen on 2023-06-06 10:49
# Source: graphql/queries.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetCampaigns(BaseModel):
    get_campaigns: Optional[List[Optional["GetCampaignsGetCampaigns"]]] = Field(
        alias="getCampaigns"
    )


class GetCampaignsGetCampaigns(BaseModel):
    id: Optional[str]
    value: Optional[str]
    key: Optional[str]
    type: Optional[str]
    description: Optional[str]
    thank_you_message: Optional[str] = Field(alias="thankYouMessage")
    already_signed_message: Optional[str] = Field(alias="alreadySignedMessage")
    close_date: Optional[Any] = Field(alias="closeDate")
    redirect_url: Optional[str] = Field(alias="redirectUrl")
    tag_user_friendly_name: Optional[str] = Field(alias="tagUserFriendlyName")
    deleted: Optional[bool]
    visible_on_preference_center: Optional[bool] = Field(
        alias="visibleOnPreferenceCenter"
    )
    short_form: Optional[bool] = Field(alias="shortForm")
    top_level_bucket_id: Optional[str] = Field(alias="topLevelBucketId")


GetCampaigns.update_forward_refs()
GetCampaignsGetCampaigns.update_forward_refs()