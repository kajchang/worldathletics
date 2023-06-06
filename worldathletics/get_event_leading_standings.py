# Generated by ariadne-codegen on 2023-06-06 10:49
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetEventLeadingStandings(BaseModel):
    get_event_leading_standings: Optional[
        List[Optional["GetEventLeadingStandingsGetEventLeadingStandings"]]
    ] = Field(alias="getEventLeadingStandings")


class GetEventLeadingStandingsGetEventLeadingStandings(BaseModel):
    event_circuit_code: Optional[str] = Field(alias="eventCircuitCode")
    sex_code: Optional[str] = Field(alias="sexCode")
    season: Optional[int]
    event_circuit_type_code: Optional[str] = Field(alias="eventCircuitTypeCode")
    rank: Optional[str]
    competitor_id: Optional[int] = Field(alias="competitorId")
    competitor_id__w_a: Optional[int] = Field(alias="competitorId_WA")
    competitor_name: Optional[str] = Field(alias="competitorName")
    competitor_country_code: Optional[str] = Field(alias="competitorCountryCode")
    total_results: Optional[int] = Field(alias="totalResults")
    total_points: Optional[str] = Field(alias="totalPoints")
    event_circuit_standing_order: Optional[int] = Field(
        alias="eventCircuitStandingOrder"
    )
    discipline: Optional["GetEventLeadingStandingsGetEventLeadingStandingsDiscipline"]


class GetEventLeadingStandingsGetEventLeadingStandingsDiscipline(BaseModel):
    name: Optional[str]


GetEventLeadingStandings.update_forward_refs()
GetEventLeadingStandingsGetEventLeadingStandings.update_forward_refs()
GetEventLeadingStandingsGetEventLeadingStandingsDiscipline.update_forward_refs()
