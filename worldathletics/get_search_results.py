# Generated by ariadne-codegen on 2024-06-04 14:46
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetSearchResults(BaseModel):
    get_search_results: Optional["GetSearchResultsGetSearchResults"] = Field(
        alias="getSearchResults"
    )


class GetSearchResultsGetSearchResults(BaseModel):
    items: Optional[List[Optional["GetSearchResultsGetSearchResultsItems"]]]


class GetSearchResultsGetSearchResultsItems(BaseModel):
    title: Optional[str]
    link: Optional[str]
    snippet: Optional[str]
    thumbnail: Optional[str]


GetSearchResults.update_forward_refs()
GetSearchResultsGetSearchResults.update_forward_refs()
GetSearchResultsGetSearchResultsItems.update_forward_refs()
