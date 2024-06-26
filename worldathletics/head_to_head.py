# Generated by ariadne-codegen on 2024-06-04 13:40
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class HeadToHead(BaseModel):
    head_to_head: Optional["HeadToHeadHeadToHead"] = Field(alias="headToHead")


class HeadToHeadHeadToHead(BaseModel):
    disciplines: Optional[List[Optional["HeadToHeadHeadToHeadDisciplines"]]]
    opponents: Optional[List[Optional["HeadToHeadHeadToHeadOpponents"]]]
    parameters: Optional["HeadToHeadHeadToHeadParameters"]
    results: Optional["HeadToHeadHeadToHeadResults"]


class HeadToHeadHeadToHeadDisciplines(BaseModel):
    id: Optional[str]
    name: Optional[str]


class HeadToHeadHeadToHeadOpponents(BaseModel):
    birth_date: Optional[str] = Field(alias="birthDate")
    country: Optional[str]
    family_name: Optional[str] = Field(alias="familyName")
    gender: Optional[str]
    given_name: Optional[str] = Field(alias="givenName")
    id: Optional[int]


class HeadToHeadHeadToHeadParameters(BaseModel):
    head_to_head_discipline: Optional[str] = Field(alias="headToHeadDiscipline")
    head_to_head_end_date: Optional[str] = Field(alias="headToHeadEndDate")
    head_to_head_final_only: Optional[bool] = Field(alias="headToHeadFinalOnly")
    head_to_head_opponent: Optional[int] = Field(alias="headToHeadOpponent")
    head_to_head_start_date: Optional[str] = Field(alias="headToHeadStartDate")


class HeadToHeadHeadToHeadResults(BaseModel):
    athlete1_wins: Optional[int] = Field(alias="athlete1Wins")
    athlete2_wins: Optional[int] = Field(alias="athlete2Wins")
    results: Optional[List[Optional["HeadToHeadHeadToHeadResultsResults"]]]


class HeadToHeadHeadToHeadResultsResults(BaseModel):
    athlete1_wins: Optional[bool] = Field(alias="athlete1Wins")
    athlete2_wins: Optional[bool] = Field(alias="athlete2Wins")
    competition: Optional[str]
    date: Optional[str]
    discipline: Optional[str]
    place1: Optional[str]
    place2: Optional[str]
    race: Optional[str]
    race_type: Optional[str] = Field(alias="raceType")
    result1: Optional[str]
    result2: Optional[str]


HeadToHead.update_forward_refs()
HeadToHeadHeadToHead.update_forward_refs()
HeadToHeadHeadToHeadDisciplines.update_forward_refs()
HeadToHeadHeadToHeadOpponents.update_forward_refs()
HeadToHeadHeadToHeadParameters.update_forward_refs()
HeadToHeadHeadToHeadResults.update_forward_refs()
HeadToHeadHeadToHeadResultsResults.update_forward_refs()
