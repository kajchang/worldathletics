# Generated by ariadne-codegen
# Source: graphql/queries.graphql

from typing import List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetCISSingleCompetitor(BaseModel):
    get_cis_single_competitor: Optional[
        "GetCISSingleCompetitorGetCisSingleCompetitor"
    ] = Field(alias="getCISSingleCompetitor")


class GetCISSingleCompetitorGetCisSingleCompetitor(BaseModel):
    basic_data: Optional["GetCISSingleCompetitorGetCisSingleCompetitorBasicData"] = (
        Field(alias="basicData")
    )
    personal_bests: Optional[
        "GetCISSingleCompetitorGetCisSingleCompetitorPersonalBests"
    ] = Field(alias="personalBests")
    seasons_bests: Optional[
        "GetCISSingleCompetitorGetCisSingleCompetitorSeasonsBests"
    ] = Field(alias="seasonsBests")
    progression_of_seasons_bests: Optional[
        List[
            Optional[
                "GetCISSingleCompetitorGetCisSingleCompetitorProgressionOfSeasonsBests"
            ]
        ]
    ] = Field(alias="progressionOfSeasonsBests")
    world_rankings: Optional[
        "GetCISSingleCompetitorGetCisSingleCompetitorWorldRankings"
    ] = Field(alias="worldRankings")
    honours: Optional[
        List[Optional["GetCISSingleCompetitorGetCisSingleCompetitorHonours"]]
    ]
    results_by_year: Optional[
        "GetCISSingleCompetitorGetCisSingleCompetitorResultsByYear"
    ] = Field(alias="resultsByYear")
    results_by_date: Optional[
        "GetCISSingleCompetitorGetCisSingleCompetitorResultsByDate"
    ] = Field(alias="resultsByDate")
    primary_media_id: Optional[str] = Field(alias="primaryMediaId")
    athlete_representative: Optional[
        "GetCISSingleCompetitorGetCisSingleCompetitorAthleteRepresentative"
    ] = Field(alias="athleteRepresentative")
    road_race_label_status: Optional[
        List[
            Optional["GetCISSingleCompetitorGetCisSingleCompetitorRoadRaceLabelStatus"]
        ]
    ] = Field(alias="roadRaceLabelStatus")


class GetCISSingleCompetitorGetCisSingleCompetitorBasicData(BaseModel):
    first_name: Optional[str] = Field(alias="firstName")
    last_name: Optional[str] = Field(alias="lastName")
    sex_name: Optional[str] = Field(alias="sexName")
    country_name: Optional[str] = Field(alias="countryName")
    country_code: Optional[str] = Field(alias="countryCode")
    country_url_slug: Optional[str] = Field(alias="countryUrlSlug")
    birth_date: Optional[str] = Field(alias="birthDate")
    birth_date_str: Optional[str] = Field(alias="birthDateStr")
    butlers_bio: Optional[str] = Field(alias="butlersBio")
    url_slug: Optional[str] = Field(alias="urlSlug")
    representative_id: Optional[int] = Field(alias="representativeId")
    biography: Optional[str]
    twitter_link: Optional[str] = Field(alias="twitterLink")
    instagram_link: Optional[str] = Field(alias="instagramLink")
    facebook_link: Optional[str] = Field(alias="facebookLink")
    iaaf_id: Optional[int] = Field(alias="iaafId")
    aa_id: Optional[int] = Field(alias="aaId")


class GetCISSingleCompetitorGetCisSingleCompetitorPersonalBests(BaseModel):
    with_wind: Optional[bool] = Field(alias="withWind")
    with_records: Optional[bool] = Field(alias="withRecords")
    results: Optional[
        List[
            Optional["GetCISSingleCompetitorGetCisSingleCompetitorPersonalBestsResults"]
        ]
    ]


class GetCISSingleCompetitorGetCisSingleCompetitorPersonalBestsResults(BaseModel):
    indoor: Optional[bool]
    discipline_code: Optional[str] = Field(alias="disciplineCode")
    discipline_name_url_slug: Optional[str] = Field(alias="disciplineNameUrlSlug")
    type_name_url_slug: Optional[str] = Field(alias="typeNameUrlSlug")
    discipline: Optional[str]
    link_to_list: Optional[bool] = Field(alias="linkToList")
    mark: Optional[str]
    combined_performances: Optional[str] = Field(alias="combinedPerformances")
    wind: Optional[str]
    not_legal: Optional[bool] = Field(alias="notLegal")
    venue: Optional[str]
    date: Optional[str]
    list_position: Optional[str] = Field(alias="listPosition")
    result_score: Optional[int] = Field(alias="resultScore")


class GetCISSingleCompetitorGetCisSingleCompetitorSeasonsBests(BaseModel):
    parameters: Optional[
        "GetCISSingleCompetitorGetCisSingleCompetitorSeasonsBestsParameters"
    ]
    active_seasons: Optional[List[Optional[str]]] = Field(alias="activeSeasons")
    with_wind: Optional[bool] = Field(alias="withWind")
    with_records: Optional[bool] = Field(alias="withRecords")
    results: Optional[
        List[
            Optional["GetCISSingleCompetitorGetCisSingleCompetitorSeasonsBestsResults"]
        ]
    ]


class GetCISSingleCompetitorGetCisSingleCompetitorSeasonsBestsParameters(BaseModel):
    seasons_bests_season: Optional[int] = Field(alias="seasonsBestsSeason")


class GetCISSingleCompetitorGetCisSingleCompetitorSeasonsBestsResults(BaseModel):
    indoor: Optional[bool]
    discipline_code: Optional[str] = Field(alias="disciplineCode")
    discipline_name_url_slug: Optional[str] = Field(alias="disciplineNameUrlSlug")
    type_name_url_slug: Optional[str] = Field(alias="typeNameUrlSlug")
    discipline: Optional[str]
    link_to_list: Optional[bool] = Field(alias="linkToList")
    mark: Optional[str]
    combined_performances: Optional[str] = Field(alias="combinedPerformances")
    wind: Optional[str]
    not_legal: Optional[bool] = Field(alias="notLegal")
    venue: Optional[str]
    date: Optional[str]
    list_position: Optional[str] = Field(alias="listPosition")
    result_score: Optional[int] = Field(alias="resultScore")


class GetCISSingleCompetitorGetCisSingleCompetitorProgressionOfSeasonsBests(BaseModel):
    indoor: Optional[bool]
    discipline_code: Optional[str] = Field(alias="disciplineCode")
    discipline_name_url_slug: Optional[str] = Field(alias="disciplineNameUrlSlug")
    type_name_url_slug: Optional[str] = Field(alias="typeNameUrlSlug")
    discipline: Optional[str]
    with_wind: Optional[bool] = Field(alias="withWind")
    main_event: Optional[bool] = Field(alias="mainEvent")
    results: Optional[
        List[
            Optional[
                "GetCISSingleCompetitorGetCisSingleCompetitorProgressionOfSeasonsBestsResults"
            ]
        ]
    ]


class GetCISSingleCompetitorGetCisSingleCompetitorProgressionOfSeasonsBestsResults(
    BaseModel
):
    season: Optional[str]
    numeric_result: Optional[float] = Field(alias="numericResult")
    mark: Optional[str]
    wind: Optional[str]
    venue: Optional[str]
    date: Optional[str]
    list_position: Optional[int] = Field(alias="listPosition")
    result_score: Optional[int] = Field(alias="resultScore")


class GetCISSingleCompetitorGetCisSingleCompetitorWorldRankings(BaseModel):
    parameters: Optional[
        "GetCISSingleCompetitorGetCisSingleCompetitorWorldRankingsParameters"
    ]
    current: Optional[
        List[
            Optional["GetCISSingleCompetitorGetCisSingleCompetitorWorldRankingsCurrent"]
        ]
    ]
    best: Optional[
        List[Optional["GetCISSingleCompetitorGetCisSingleCompetitorWorldRankingsBest"]]
    ]


class GetCISSingleCompetitorGetCisSingleCompetitorWorldRankingsParameters(BaseModel):
    world_rankings_progression_year: Optional[int] = Field(
        alias="worldRankingsProgressionYear"
    )


class GetCISSingleCompetitorGetCisSingleCompetitorWorldRankingsCurrent(BaseModel):
    ranking_calculation_id: Optional[str] = Field(alias="rankingCalculationId")
    event_group: Optional[str] = Field(alias="eventGroup")
    male: Optional[bool]
    url_slug: Optional[str] = Field(alias="urlSlug")
    place: Optional[int]
    ranking_score: Optional[int] = Field(alias="rankingScore")


class GetCISSingleCompetitorGetCisSingleCompetitorWorldRankingsBest(BaseModel):
    event_group: Optional[str] = Field(alias="eventGroup")
    event_group_id: Optional[int] = Field(alias="eventGroupId")
    url_slug: Optional[str] = Field(alias="urlSlug")
    place: Optional[str]
    weeks: Optional[int]


class GetCISSingleCompetitorGetCisSingleCompetitorHonours(BaseModel):
    category_name: Optional[str] = Field(alias="categoryName")
    with_wind: Optional[bool] = Field(alias="withWind")
    with_drop: Optional[bool] = Field(alias="withDrop")
    results: Optional[
        List[Optional["GetCISSingleCompetitorGetCisSingleCompetitorHonoursResults"]]
    ]


class GetCISSingleCompetitorGetCisSingleCompetitorHonoursResults(BaseModel):
    place: Optional[str]
    indoor: Optional[bool]
    discipline_code: Optional[str] = Field(alias="disciplineCode")
    discipline_name_url_slug: Optional[str] = Field(alias="disciplineNameUrlSlug")
    type_name_url_slug: Optional[str] = Field(alias="typeNameUrlSlug")
    discipline: Optional[str]
    competition: Optional[str]
    venue: Optional[str]
    mark: Optional[str]
    wind: Optional[str]
    date: Optional[str]


class GetCISSingleCompetitorGetCisSingleCompetitorResultsByYear(BaseModel):
    parameters: Optional[
        "GetCISSingleCompetitorGetCisSingleCompetitorResultsByYearParameters"
    ]
    active_years: Optional[List[Optional[str]]] = Field(alias="activeYears")
    results_by_event: Optional[
        List[
            Optional[
                "GetCISSingleCompetitorGetCisSingleCompetitorResultsByYearResultsByEvent"
            ]
        ]
    ] = Field(alias="resultsByEvent")


class GetCISSingleCompetitorGetCisSingleCompetitorResultsByYearParameters(BaseModel):
    results_by_year: Optional[int] = Field(alias="resultsByYear")
    results_by_year_order_by: Optional[str] = Field(alias="resultsByYearOrderBy")


class GetCISSingleCompetitorGetCisSingleCompetitorResultsByYearResultsByEvent(
    BaseModel
):
    indoor: Optional[bool]
    discipline_code: Optional[str] = Field(alias="disciplineCode")
    discipline_name_url_slug: Optional[str] = Field(alias="disciplineNameUrlSlug")
    type_name_url_slug: Optional[str] = Field(alias="typeNameUrlSlug")
    discipline: Optional[str]
    with_wind: Optional[bool] = Field(alias="withWind")
    with_remark: Optional[bool] = Field(alias="withRemark")
    results: Optional[
        List[
            Optional[
                "GetCISSingleCompetitorGetCisSingleCompetitorResultsByYearResultsByEventResults"
            ]
        ]
    ]


class GetCISSingleCompetitorGetCisSingleCompetitorResultsByYearResultsByEventResults(
    BaseModel
):
    date: Optional[str]
    competition: Optional[str]
    venue: Optional[str]
    country: Optional[str]
    category: Optional[str]
    race: Optional[str]
    place: Optional[str]
    mark: Optional[str]
    wind: Optional[str]
    not_legal: Optional[bool] = Field(alias="notLegal")
    result_score: Optional[int] = Field(alias="resultScore")
    remark: Optional[str]


class GetCISSingleCompetitorGetCisSingleCompetitorResultsByDate(BaseModel):
    parameters: Optional[
        "GetCISSingleCompetitorGetCisSingleCompetitorResultsByDateParameters"
    ]
    active_years: Optional[List[Optional[str]]] = Field(alias="activeYears")
    with_remark: Optional[bool] = Field(alias="withRemark")
    results_by_date: Optional[
        List[
            Optional[
                "GetCISSingleCompetitorGetCisSingleCompetitorResultsByDateResultsByDate"
            ]
        ]
    ] = Field(alias="resultsByDate")


class GetCISSingleCompetitorGetCisSingleCompetitorResultsByDateParameters(BaseModel):
    results_by_year: Optional[int] = Field(alias="resultsByYear")
    results_by_year_order_by: Optional[str] = Field(alias="resultsByYearOrderBy")


class GetCISSingleCompetitorGetCisSingleCompetitorResultsByDateResultsByDate(BaseModel):
    date: Optional[str]
    competition: Optional[str]
    venue: Optional[str]
    indoor: Optional[bool]
    discipline_code: Optional[str] = Field(alias="disciplineCode")
    discipline_name_url_slug: Optional[str] = Field(alias="disciplineNameUrlSlug")
    type_name_url_slug: Optional[str] = Field(alias="typeNameUrlSlug")
    discipline: Optional[str]
    country: Optional[str]
    category: Optional[str]
    race: Optional[str]
    place: Optional[str]
    mark: Optional[str]
    wind: Optional[str]
    not_legal: Optional[bool] = Field(alias="notLegal")
    result_score: Optional[int] = Field(alias="resultScore")
    remark: Optional[str]


class GetCISSingleCompetitorGetCisSingleCompetitorAthleteRepresentative(BaseModel):
    name: Optional[str]
    country_code: Optional[str] = Field(alias="countryCode")
    country_name: Optional[str] = Field(alias="countryName")
    email: Optional[str]
    telephone: Optional[str]
    mobile: Optional[str]
    rep_email: Optional[str] = Field(alias="repEmail")
    website: Optional[str]


class GetCISSingleCompetitorGetCisSingleCompetitorRoadRaceLabelStatus(BaseModel):
    year: Optional[str]
    label_status: Optional[str] = Field(alias="labelStatus")


GetCISSingleCompetitor.model_rebuild()
GetCISSingleCompetitorGetCisSingleCompetitor.model_rebuild()
GetCISSingleCompetitorGetCisSingleCompetitorPersonalBests.model_rebuild()
GetCISSingleCompetitorGetCisSingleCompetitorSeasonsBests.model_rebuild()
GetCISSingleCompetitorGetCisSingleCompetitorProgressionOfSeasonsBests.model_rebuild()
GetCISSingleCompetitorGetCisSingleCompetitorWorldRankings.model_rebuild()
GetCISSingleCompetitorGetCisSingleCompetitorHonours.model_rebuild()
GetCISSingleCompetitorGetCisSingleCompetitorResultsByYear.model_rebuild()
GetCISSingleCompetitorGetCisSingleCompetitorResultsByYearResultsByEvent.model_rebuild()
GetCISSingleCompetitorGetCisSingleCompetitorResultsByDate.model_rebuild()
