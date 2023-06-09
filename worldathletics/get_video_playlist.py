# Generated by ariadne-codegen on 2023-06-06 10:50
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetVideoPlaylist(BaseModel):
    get_video_playlist: Optional[
        List[Optional["GetVideoPlaylistGetVideoPlaylist"]]
    ] = Field(alias="getVideoPlaylist")


class GetVideoPlaylistGetVideoPlaylist(BaseModel):
    id: Optional[str]
    title: Optional[str]
    slug: Optional[str]


GetVideoPlaylist.update_forward_refs()
GetVideoPlaylistGetVideoPlaylist.update_forward_refs()
