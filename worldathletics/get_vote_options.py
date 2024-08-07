# Generated by ariadne-codegen
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetVoteOptions(BaseModel):
    get_vote_options: Optional[List[Optional["GetVoteOptionsGetVoteOptions"]]] = Field(
        alias="getVoteOptions"
    )


class GetVoteOptionsGetVoteOptions(BaseModel):
    id: Optional[str]
    order: Optional[int]
    vote_id: Optional[str] = Field(alias="voteId")
    vote_name: Optional[str] = Field(alias="voteName")
    option_year: Optional[int] = Field(alias="optionYear")
    option_athlete_name: Optional[str] = Field(alias="optionAthleteName")
    option_description: Optional[str] = Field(alias="optionDescription")
    image_url: Optional[str] = Field(alias="imageUrl")
    votes_count: Optional[int] = Field(alias="votesCount")


GetVoteOptions.model_rebuild()
