# Generated by ariadne-codegen on 2023-06-06 10:50
# Source: graphql/queries.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetLiveBlogPosts(BaseModel):
    get_live_blog_posts: Optional[
        List[Optional["GetLiveBlogPostsGetLiveBlogPosts"]]
    ] = Field(alias="getLiveBlogPosts")


class GetLiveBlogPostsGetLiveBlogPosts(BaseModel):
    id: Optional[str]
    parent_id: Optional[str] = Field(alias="parentId")
    post_id: Optional[str] = Field(alias="postId")
    language: Optional[str]
    title: Optional[str]
    image_id: Optional[str] = Field(alias="imageId")
    image_edited: Optional[str] = Field(alias="imageEdited")
    text: Optional[str]
    date_time: Optional[Any] = Field(alias="dateTime")


GetLiveBlogPosts.update_forward_refs()
GetLiveBlogPostsGetLiveBlogPosts.update_forward_refs()