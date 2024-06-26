# Generated by ariadne-codegen on 2024-06-04 13:40
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetAthleteRepresentativeDirectory(BaseModel):
    get_athlete_representative_directory: Optional[
        List[
            Optional[
                "GetAthleteRepresentativeDirectoryGetAthleteRepresentativeDirectory"
            ]
        ]
    ] = Field(alias="getAthleteRepresentativeDirectory")


class GetAthleteRepresentativeDirectoryGetAthleteRepresentativeDirectory(BaseModel):
    athlete_representative_id: Optional[int] = Field(alias="athleteRepresentativeId")
    country_code: Optional[str] = Field(alias="countryCode")
    first_name: Optional[str] = Field(alias="firstName")
    birthdate: Optional[str]
    athlete_id: Optional[int] = Field(alias="athleteId")
    last_name: Optional[str] = Field(alias="lastName")
    country: Optional[str]
    gender: Optional[str]
    expiry: Optional[str]


GetAthleteRepresentativeDirectory.update_forward_refs()
GetAthleteRepresentativeDirectoryGetAthleteRepresentativeDirectory.update_forward_refs()
