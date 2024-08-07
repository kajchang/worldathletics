# Generated by ariadne-codegen
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetAthleteRepresentativeAthleteSearch(BaseModel):
    get_athlete_representative_athlete_search: Optional[
        "GetAthleteRepresentativeAthleteSearchGetAthleteRepresentativeAthleteSearch"
    ] = Field(alias="getAthleteRepresentativeAthleteSearch")


class GetAthleteRepresentativeAthleteSearchGetAthleteRepresentativeAthleteSearch(
    BaseModel
):
    countries: Optional[
        List[
            Optional[
                "GetAthleteRepresentativeAthleteSearchGetAthleteRepresentativeAthleteSearchCountries"
            ]
        ]
    ]
    athletes: Optional[
        List[
            Optional[
                "GetAthleteRepresentativeAthleteSearchGetAthleteRepresentativeAthleteSearchAthletes"
            ]
        ]
    ]


class GetAthleteRepresentativeAthleteSearchGetAthleteRepresentativeAthleteSearchCountries(
    BaseModel
):
    country: Optional[str]
    country_code: Optional[str] = Field(alias="countryCode")


class GetAthleteRepresentativeAthleteSearchGetAthleteRepresentativeAthleteSearchAthletes(
    BaseModel
):
    group: Optional[str]
    children: Optional[
        List[
            Optional[
                "GetAthleteRepresentativeAthleteSearchGetAthleteRepresentativeAthleteSearchAthletesChildren"
            ]
        ]
    ]


class GetAthleteRepresentativeAthleteSearchGetAthleteRepresentativeAthleteSearchAthletesChildren(
    BaseModel
):
    athlete_representative_id: Optional[int] = Field(alias="athleteRepresentativeId")
    country_code: Optional[str] = Field(alias="countryCode")
    first_name: Optional[str] = Field(alias="firstName")
    birthdate: Optional[str]
    athlete_id: Optional[int] = Field(alias="athleteId")
    last_name: Optional[str] = Field(alias="lastName")
    country: Optional[str]
    gender: Optional[str]
    expiry: Optional[str]


GetAthleteRepresentativeAthleteSearch.model_rebuild()
GetAthleteRepresentativeAthleteSearchGetAthleteRepresentativeAthleteSearch.model_rebuild()
GetAthleteRepresentativeAthleteSearchGetAthleteRepresentativeAthleteSearchAthletes.model_rebuild()
