# Generated by ariadne-codegen on 2023-06-06 10:50
# Source: graphql/queries.graphql

from typing import Any, Optional

from pydantic import Field

from .base_model import BaseModel


class GetVocabulary(BaseModel):
    get_vocabulary: Optional["GetVocabularyGetVocabulary"] = Field(
        alias="getVocabulary"
    )


class GetVocabularyGetVocabulary(BaseModel):
    vocabulary: Optional[Any]


GetVocabulary.update_forward_refs()
GetVocabularyGetVocabulary.update_forward_refs()
