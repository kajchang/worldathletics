# Generated by ariadne-codegen on 2024-06-04 13:40
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class VerifyHCaptchaToken(BaseModel):
    verify_h_captcha_token: Optional["VerifyHCaptchaTokenVerifyHCaptchaToken"] = Field(
        alias="verifyHCaptchaToken"
    )


class VerifyHCaptchaTokenVerifyHCaptchaToken(BaseModel):
    is_success: Optional[bool] = Field(alias="isSuccess")
    error_codes: Optional[List[Optional[str]]] = Field(alias="errorCodes")
    hostname: Optional[str]


VerifyHCaptchaToken.update_forward_refs()
VerifyHCaptchaTokenVerifyHCaptchaToken.update_forward_refs()
