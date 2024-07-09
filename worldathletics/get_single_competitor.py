# Generated by ariadne-codegen on 2024-06-04 14:46
# Source: graphql/queries.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetSingleCompetitor(BaseModel):
    get_single_competitor: Optional["GetSingleCompetitorGetSingleCompetitor"] = Field(
        alias="getSingleCompetitor"
    )


class GetSingleCompetitorGetSingleCompetitor(BaseModel):
    id: Optional[int] = Field(alias="_id")
    basic_data: Optional["GetSingleCompetitorGetSingleCompetitorBasicData"] = Field(
        alias="basicData"
    )
    personal_bests: Optional["GetSingleCompetitorGetSingleCompetitorPersonalBests"] = (
        Field(alias="personalBests")
    )
    seasons_bests: Optional["GetSingleCompetitorGetSingleCompetitorSeasonsBests"] = (
        Field(alias="seasonsBests")
    )
    progression_of_seasons_bests: Optional[
        List[
            Optional["GetSingleCompetitorGetSingleCompetitorProgressionOfSeasonsBests"]
        ]
    ] = Field(alias="progressionOfSeasonsBests")
    world_rankings: Optional["GetSingleCompetitorGetSingleCompetitorWorldRankings"] = (
        Field(alias="worldRankings")
    )
    honours: Optional[List[Optional["GetSingleCompetitorGetSingleCompetitorHonours"]]]
    results_by_year: Optional["GetSingleCompetitorGetSingleCompetitorResultsByYear"] = (
        Field(alias="resultsByYear")
    )
    results_by_date: Optional["GetSingleCompetitorGetSingleCompetitorResultsByDate"] = (
        Field(alias="resultsByDate")
    )
    primary_media_id: Optional[List[Optional[str]]] = Field(alias="primaryMediaId")
    primary_media_id2: Optional[bool] = Field(alias="primaryMediaId2")
    primary_media: Optional[
        List[Optional["GetSingleCompetitorGetSingleCompetitorPrimaryMedia"]]
    ] = Field(alias="primaryMedia")
    athlete_representative: Optional[
        "GetSingleCompetitorGetSingleCompetitorAthleteRepresentative"
    ] = Field(alias="athleteRepresentative")


class GetSingleCompetitorGetSingleCompetitorBasicData(BaseModel):
    id: Optional[int]
    iaaf_id: Optional[int] = Field(alias="iaafId")
    first_name: Optional[str] = Field(alias="firstName")
    last_name: Optional[str] = Field(alias="lastName")
    friendly_name: Optional[str] = Field(alias="friendlyName")
    full_name: Optional[str] = Field(alias="fullName")
    friendly_name_letter: Optional[str] = Field(alias="friendlyNameLetter")
    friendly_name_first3_letter: Optional[str] = Field(alias="friendlyNameFirst3Letter")
    sex_code: Optional[str] = Field(alias="sexCode")
    sex_name: Optional[str] = Field(alias="sexName")
    country_code: Optional[str] = Field(alias="countryCode")
    country_name: Optional[str] = Field(alias="countryName")
    birth_date: Optional[str] = Field(alias="birthDate")
    birth_place: Optional[str] = Field(alias="birthPlace")
    birth_place_country_name: Optional[str] = Field(alias="birthPlaceCountryName")
    sex_name_url_slug: Optional[str] = Field(alias="sexNameUrlSlug")
    country_url_slug: Optional[str] = Field(alias="countryUrlSlug")
    birth_place_country_url_slug: Optional[str] = Field(
        alias="birthPlaceCountryUrlSlug"
    )
    birth_country_code: Optional[str] = Field(alias="birthCountryCode")
    primary_media_id: Optional[str] = Field(alias="primaryMediaId")
    primary_media_edited: Optional[str] = Field(alias="primaryMediaEdited")
    primary_media: Optional[
        List[Optional["GetSingleCompetitorGetSingleCompetitorBasicDataPrimaryMedia"]]
    ] = Field(alias="primaryMedia")
    url_slug: Optional[str] = Field(alias="urlSlug")
    representative_id: Optional[int] = Field(alias="representativeId")
    biography: Optional[str]
    twitter_link: Optional[str] = Field(alias="twitterLink")
    instagram_link: Optional[str] = Field(alias="instagramLink")
    facebook_link: Optional[str] = Field(alias="facebookLink")
    transfers_of_allegiance: Optional[List[Optional[str]]] = Field(
        alias="transfersOfAllegiance"
    )
    aa_id: Optional[int] = Field(alias="aaId")
    country_full_name: Optional[str] = Field(alias="countryFullName")
    family_name: Optional[str] = Field(alias="familyName")
    given_name: Optional[str] = Field(alias="givenName")
    birth_date_str: Optional[str] = Field(alias="birthDateStr")
    facebook_username: Optional[str] = Field(alias="facebookUsername")
    twitter_username: Optional[str] = Field(alias="twitterUsername")
    instagram_username: Optional[str] = Field(alias="instagramUsername")
    male: Optional[bool]
    media_ids: Optional[List[Optional[str]]] = Field(alias="mediaIds")


class GetSingleCompetitorGetSingleCompetitorBasicDataPrimaryMedia(BaseModel):
    id: Optional[str]
    title: Optional[str]
    s_e_o_title: Optional[str] = Field(alias="sEOTitle")
    url_slug: Optional[str] = Field(alias="urlSlug")
    credit: Optional[str]
    show_in_media: Optional[bool] = Field(alias="showInMedia")
    complete: Optional[bool]
    file_name: Optional[str] = Field(alias="fileName")
    remote_item_code: Optional[str] = Field(alias="remoteItemCode")
    x_m_l_file_name360: Optional[str] = Field(alias="xMLFileName360")
    file_name_url: Optional[str] = Field(alias="fileNameUrl")
    type: Optional[int]
    format: Optional[int]
    hosting: Optional[int]
    related_links: Optional[List[Optional[str]]] = Field(alias="relatedLinks")
    source_width: Optional[int] = Field(alias="sourceWidth")
    source_height: Optional[int] = Field(alias="sourceHeight")
    available_ratios: Optional[List[Optional[int]]] = Field(alias="availableRatios")
    related_sex_codes: Optional[List[Optional[int]]] = Field(alias="relatedSexCodes")
    related_age_groups: Optional[List[Optional[int]]] = Field(alias="relatedAgeGroups")
    related_event_phases: Optional[List[Optional[int]]] = Field(
        alias="relatedEventPhases"
    )
    status: Optional[int]
    live_from: Optional[Any] = Field(alias="liveFrom")
    created_on: Optional[str] = Field(alias="createdOn")
    updated_on: Optional[Any] = Field(alias="updatedOn")
    created_by_id: Optional[str] = Field(alias="createdById")
    updated_by_id: Optional[str] = Field(alias="updatedById")


class GetSingleCompetitorGetSingleCompetitorPersonalBests(BaseModel):
    with_wind: Optional[bool] = Field(alias="withWind")
    with_records: Optional[bool] = Field(alias="withRecords")
    results: Optional[
        List[Optional["GetSingleCompetitorGetSingleCompetitorPersonalBestsResults"]]
    ]


class GetSingleCompetitorGetSingleCompetitorPersonalBestsResults(BaseModel):
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
    event_id: Optional[str] = Field(alias="eventId")
    competition_id: Optional[str] = Field(alias="competitionId")
    records: Optional[List[Optional[str]]]


class GetSingleCompetitorGetSingleCompetitorSeasonsBests(BaseModel):
    parameters: Optional["GetSingleCompetitorGetSingleCompetitorSeasonsBestsParameters"]
    active_seasons: Optional[List[Optional[str]]] = Field(alias="activeSeasons")
    with_wind: Optional[bool] = Field(alias="withWind")
    with_records: Optional[bool] = Field(alias="withRecords")
    results: Optional[
        List[Optional["GetSingleCompetitorGetSingleCompetitorSeasonsBestsResults"]]
    ]


class GetSingleCompetitorGetSingleCompetitorSeasonsBestsParameters(BaseModel):
    seasons_bests_season: Optional[int] = Field(alias="seasonsBestsSeason")


class GetSingleCompetitorGetSingleCompetitorSeasonsBestsResults(BaseModel):
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
    event_id: Optional[str] = Field(alias="eventId")
    competition_id: Optional[str] = Field(alias="competitionId")
    records: Optional[List[Optional[str]]]


class GetSingleCompetitorGetSingleCompetitorProgressionOfSeasonsBests(BaseModel):
    indoor: Optional[bool]
    discipline_code: Optional[str] = Field(alias="disciplineCode")
    discipline_name_url_slug: Optional[str] = Field(alias="disciplineNameUrlSlug")
    type_name_url_slug: Optional[str] = Field(alias="typeNameUrlSlug")
    discipline: Optional[str]
    with_wind: Optional[bool] = Field(alias="withWind")
    main_event: Optional[bool] = Field(alias="mainEvent")
    event_id: Optional[str] = Field(alias="eventId")
    results: Optional[
        List[
            Optional[
                "GetSingleCompetitorGetSingleCompetitorProgressionOfSeasonsBestsResults"
            ]
        ]
    ]


class GetSingleCompetitorGetSingleCompetitorProgressionOfSeasonsBestsResults(BaseModel):
    season: Optional[str]
    numeric_result: Optional[float] = Field(alias="numericResult")
    mark: Optional[str]
    wind: Optional[str]
    venue: Optional[str]
    date: Optional[str]
    list_position: Optional[int] = Field(alias="listPosition")
    result_score: Optional[int] = Field(alias="resultScore")
    competition_id: Optional[str] = Field(alias="competitionId")


class GetSingleCompetitorGetSingleCompetitorWorldRankings(BaseModel):
    parameters: Optional[
        "GetSingleCompetitorGetSingleCompetitorWorldRankingsParameters"
    ]
    current: Optional[
        List[Optional["GetSingleCompetitorGetSingleCompetitorWorldRankingsCurrent"]]
    ]
    best: Optional[
        List[Optional["GetSingleCompetitorGetSingleCompetitorWorldRankingsBest"]]
    ]


class GetSingleCompetitorGetSingleCompetitorWorldRankingsParameters(BaseModel):
    world_rankings_progression_year: Optional[int] = Field(
        alias="worldRankingsProgressionYear"
    )


class GetSingleCompetitorGetSingleCompetitorWorldRankingsCurrent(BaseModel):
    ranking_calculation_id: Optional[str] = Field(alias="rankingCalculationId")
    event_group: Optional[str] = Field(alias="eventGroup")
    male: Optional[bool]
    url_slug: Optional[str] = Field(alias="urlSlug")
    place: Optional[int]
    ranking_score: Optional[int] = Field(alias="rankingScore")


class GetSingleCompetitorGetSingleCompetitorWorldRankingsBest(BaseModel):
    event_group: Optional[str] = Field(alias="eventGroup")
    event_group_id: Optional[int] = Field(alias="eventGroupId")
    url_slug: Optional[str] = Field(alias="urlSlug")
    place: Optional[str]
    weeks: Optional[int]


class GetSingleCompetitorGetSingleCompetitorHonours(BaseModel):
    category_name: Optional[str] = Field(alias="categoryName")
    with_wind: Optional[bool] = Field(alias="withWind")
    with_drop: Optional[bool] = Field(alias="withDrop")
    results: Optional[
        List[Optional["GetSingleCompetitorGetSingleCompetitorHonoursResults"]]
    ]


class GetSingleCompetitorGetSingleCompetitorHonoursResults(BaseModel):
    place: Optional[str]
    indoor: Optional[bool]
    discipline_code: Optional[str] = Field(alias="disciplineCode")
    discipline_name_url_slug: Optional[str] = Field(alias="disciplineNameUrlSlug")
    type_name_url_slug: Optional[str] = Field(alias="typeNameUrlSlug")
    discipline: Optional[str]
    competition: Optional[str]
    venue: Optional[str]
    mark: Optional[str]
    date: Optional[str]
    competition_id: Optional[str] = Field(alias="competitionId")
    event_id: Optional[str] = Field(alias="eventId")


class GetSingleCompetitorGetSingleCompetitorResultsByYear(BaseModel):
    parameters: Optional[
        "GetSingleCompetitorGetSingleCompetitorResultsByYearParameters"
    ]
    active_years: Optional[List[Optional[str]]] = Field(alias="activeYears")
    results_by_event: Optional[
        List[
            Optional[
                "GetSingleCompetitorGetSingleCompetitorResultsByYearResultsByEvent"
            ]
        ]
    ] = Field(alias="resultsByEvent")


class GetSingleCompetitorGetSingleCompetitorResultsByYearParameters(BaseModel):
    results_by_year: Optional[int] = Field(alias="resultsByYear")
    results_by_year_order_by: Optional[str] = Field(alias="resultsByYearOrderBy")


class GetSingleCompetitorGetSingleCompetitorResultsByYearResultsByEvent(BaseModel):
    indoor: Optional[bool]
    discipline_code: Optional[str] = Field(alias="disciplineCode")
    discipline_name_url_slug: Optional[str] = Field(alias="disciplineNameUrlSlug")
    type_name_url_slug: Optional[str] = Field(alias="typeNameUrlSlug")
    discipline: Optional[str]
    with_wind: Optional[bool] = Field(alias="withWind")
    results: Optional[
        List[
            Optional[
                "GetSingleCompetitorGetSingleCompetitorResultsByYearResultsByEventResults"
            ]
        ]
    ]


class GetSingleCompetitorGetSingleCompetitorResultsByYearResultsByEventResults(
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
    competition_id: Optional[str] = Field(alias="competitionId")
    event_id: Optional[str] = Field(alias="eventId")


class GetSingleCompetitorGetSingleCompetitorResultsByDate(BaseModel):
    parameters: Optional[
        "GetSingleCompetitorGetSingleCompetitorResultsByDateParameters"
    ]
    active_years: Optional[List[Optional[str]]] = Field(alias="activeYears")
    results_by_date: Optional[
        List[
            Optional["GetSingleCompetitorGetSingleCompetitorResultsByDateResultsByDate"]
        ]
    ] = Field(alias="resultsByDate")


class GetSingleCompetitorGetSingleCompetitorResultsByDateParameters(BaseModel):
    results_by_year: Optional[int] = Field(alias="resultsByYear")
    results_by_year_order_by: Optional[str] = Field(alias="resultsByYearOrderBy")


class GetSingleCompetitorGetSingleCompetitorResultsByDateResultsByDate(BaseModel):
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
    competition_id: Optional[str] = Field(alias="competitionId")
    event_id: Optional[str] = Field(alias="eventId")


class GetSingleCompetitorGetSingleCompetitorPrimaryMedia(BaseModel):
    id: Optional[str]
    title: Optional[str]
    s_e_o_title: Optional[str] = Field(alias="sEOTitle")
    url_slug: Optional[str] = Field(alias="urlSlug")
    credit: Optional[str]
    show_in_media: Optional[bool] = Field(alias="showInMedia")
    complete: Optional[bool]
    file_name: Optional[str] = Field(alias="fileName")
    remote_item_code: Optional[str] = Field(alias="remoteItemCode")
    x_m_l_file_name360: Optional[str] = Field(alias="xMLFileName360")
    file_name_url: Optional[str] = Field(alias="fileNameUrl")
    type: Optional[int]
    format: Optional[int]
    hosting: Optional[int]
    related_links: Optional[List[Optional[str]]] = Field(alias="relatedLinks")
    source_width: Optional[int] = Field(alias="sourceWidth")
    source_height: Optional[int] = Field(alias="sourceHeight")
    available_ratios: Optional[List[Optional[int]]] = Field(alias="availableRatios")
    related_sex_codes: Optional[List[Optional[int]]] = Field(alias="relatedSexCodes")
    related_age_groups: Optional[List[Optional[int]]] = Field(alias="relatedAgeGroups")
    related_event_phases: Optional[List[Optional[int]]] = Field(
        alias="relatedEventPhases"
    )
    status: Optional[int]
    live_from: Optional[Any] = Field(alias="liveFrom")
    created_on: Optional[str] = Field(alias="createdOn")
    updated_on: Optional[Any] = Field(alias="updatedOn")
    created_by_id: Optional[str] = Field(alias="createdById")
    updated_by_id: Optional[str] = Field(alias="updatedById")


class GetSingleCompetitorGetSingleCompetitorAthleteRepresentative(BaseModel):
    id: Optional[int] = Field(alias="_id")
    name: Optional[str]
    country_code: Optional[str] = Field(alias="countryCode")
    country_name: Optional[str] = Field(alias="countryName")
    email: Optional[str]
    telephone: Optional[str]
    mobile: Optional[str]
    website: Optional[List[Optional[str]]]


GetSingleCompetitor.update_forward_refs()
GetSingleCompetitorGetSingleCompetitor.update_forward_refs()
GetSingleCompetitorGetSingleCompetitorBasicData.update_forward_refs()
GetSingleCompetitorGetSingleCompetitorBasicDataPrimaryMedia.update_forward_refs()
GetSingleCompetitorGetSingleCompetitorPersonalBests.update_forward_refs()
GetSingleCompetitorGetSingleCompetitorPersonalBestsResults.update_forward_refs()
GetSingleCompetitorGetSingleCompetitorSeasonsBests.update_forward_refs()
GetSingleCompetitorGetSingleCompetitorSeasonsBestsParameters.update_forward_refs()
GetSingleCompetitorGetSingleCompetitorSeasonsBestsResults.update_forward_refs()
GetSingleCompetitorGetSingleCompetitorProgressionOfSeasonsBests.update_forward_refs()
GetSingleCompetitorGetSingleCompetitorProgressionOfSeasonsBestsResults.update_forward_refs()
GetSingleCompetitorGetSingleCompetitorWorldRankings.update_forward_refs()
GetSingleCompetitorGetSingleCompetitorWorldRankingsParameters.update_forward_refs()
GetSingleCompetitorGetSingleCompetitorWorldRankingsCurrent.update_forward_refs()
GetSingleCompetitorGetSingleCompetitorWorldRankingsBest.update_forward_refs()
GetSingleCompetitorGetSingleCompetitorHonours.update_forward_refs()
GetSingleCompetitorGetSingleCompetitorHonoursResults.update_forward_refs()
GetSingleCompetitorGetSingleCompetitorResultsByYear.update_forward_refs()
GetSingleCompetitorGetSingleCompetitorResultsByYearParameters.update_forward_refs()
GetSingleCompetitorGetSingleCompetitorResultsByYearResultsByEvent.update_forward_refs()
GetSingleCompetitorGetSingleCompetitorResultsByYearResultsByEventResults.update_forward_refs()
GetSingleCompetitorGetSingleCompetitorResultsByDate.update_forward_refs()
GetSingleCompetitorGetSingleCompetitorResultsByDateParameters.update_forward_refs()
GetSingleCompetitorGetSingleCompetitorResultsByDateResultsByDate.update_forward_refs()
GetSingleCompetitorGetSingleCompetitorPrimaryMedia.update_forward_refs()
GetSingleCompetitorGetSingleCompetitorAthleteRepresentative.update_forward_refs()
