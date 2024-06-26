# Generated by ariadne-codegen on 2024-06-04 13:40
# Source: graphql/queries.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetAllCompetitions(BaseModel):
    get_all_competitions: Optional["GetAllCompetitionsGetAllCompetitions"] = Field(
        alias="getAllCompetitions"
    )


class GetAllCompetitionsGetAllCompetitions(BaseModel):
    page_next_event: Optional["GetAllCompetitionsGetAllCompetitionsPageNextEvent"] = (
        Field(alias="pageNextEvent")
    )
    all_events: Optional[
        List[Optional["GetAllCompetitionsGetAllCompetitionsAllEvents"]]
    ] = Field(alias="allEvents")


class GetAllCompetitionsGetAllCompetitionsPageNextEvent(BaseModel):
    id: Optional[str]
    name: Optional[str]
    circuit_type_code: Optional[str] = Field(alias="circuitTypeCode")
    event_sub_category_code: Optional[str] = Field(alias="eventSubCategoryCode")
    description: Optional[str]
    circuit_code: Optional[str] = Field(alias="circuitCode")
    url_slug: Optional[str] = Field(alias="urlSlug")
    order: Optional[int]
    category: Optional[int]
    about: Optional[str]
    primary_media_id: Optional[str] = Field(alias="primaryMediaId")
    related_media_ids: Optional[List[Optional[str]]] = Field(alias="relatedMediaIds")
    logo_light_id: Optional[str] = Field(alias="logoLightId")
    logo_dark_id: Optional[str] = Field(alias="logoDarkId")
    style_overrides: Optional[str] = Field(alias="styleOverrides")
    related_info: Optional[List[Optional[str]]] = Field(alias="relatedInfo")
    next_event: Optional[
        "GetAllCompetitionsGetAllCompetitionsPageNextEventNextEvent"
    ] = Field(alias="nextEvent")
    last_event: Optional[
        "GetAllCompetitionsGetAllCompetitionsPageNextEventLastEvent"
    ] = Field(alias="lastEvent")
    next_event_start_date: Optional[Any] = Field(alias="nextEventStartDate")
    page_id: Optional[str] = Field(alias="pageId")
    page: Optional["GetAllCompetitionsGetAllCompetitionsPageNextEventPage"]


class GetAllCompetitionsGetAllCompetitionsPageNextEventNextEvent(BaseModel):
    id: Optional[int]
    updated_on: Optional[Any] = Field(alias="updatedOn")
    name: Optional[str]
    start_date: Optional[Any] = Field(alias="startDate")
    end_date: Optional[Any] = Field(alias="endDate")
    hash: Optional[str]
    venue: Optional[str]
    country_code: Optional[str] = Field(alias="countryCode")
    country_name: Optional[str] = Field(alias="countryName")
    area_code: Optional[str] = Field(alias="areaCode")
    area_name: Optional[str] = Field(alias="areaName")
    age_code: Optional[str] = Field(alias="ageCode")
    indoor_outdoor: Optional[str] = Field(alias="indoorOutdoor")
    category_code: Optional[str] = Field(alias="categoryCode")
    category_name: Optional[str] = Field(alias="categoryName")
    category_order: Optional[int] = Field(alias="categoryOrder")
    sub_category_code: Optional[str] = Field(alias="subCategoryCode")
    sub_category_name: Optional[str] = Field(alias="subCategoryName")
    show_web_live_banner: Optional[bool] = Field(alias="showWebLiveBanner")
    sub_category_order: Optional[int] = Field(alias="subCategoryOrder")
    class_code: Optional[str] = Field(alias="classCode")
    class_order: Optional[int] = Field(alias="classOrder")
    is_published: Optional[bool] = Field(alias="isPublished")
    has_comp_doc_results: Optional[bool] = Field(alias="hasCompDocResults")
    name_url_slug: Optional[str] = Field(alias="nameUrlSlug")
    start_date_year: Optional[int] = Field(alias="startDateYear")
    circuits: Optional[
        List[
            Optional[
                "GetAllCompetitionsGetAllCompetitionsPageNextEventNextEventCircuits"
            ]
        ]
    ]
    area_name_url_slug: Optional[str] = Field(alias="areaNameUrlSlug")
    category_name_url_slug: Optional[str] = Field(alias="categoryNameUrlSlug")
    sub_category_name_url_slug: Optional[str] = Field(alias="subCategoryNameUrlSlug")
    discipline_codes: Optional[List[Optional[str]]] = Field(alias="disciplineCodes")
    event_id__w_a: Optional[int] = Field(alias="eventId_WA")
    has_timetable: Optional[bool] = Field(alias="hasTimetable")
    page: Optional["GetAllCompetitionsGetAllCompetitionsPageNextEventNextEventPage"]
    event_start_date_time: Optional[Any] = Field(alias="eventStartDateTime")
    event_end_date_time: Optional[Any] = Field(alias="eventEndDateTime")
    venue_timezone: Optional[str] = Field(alias="venueTimezone")
    banner_lead_time_in_hours: Optional[int] = Field(alias="bannerLeadTimeInHours")


class GetAllCompetitionsGetAllCompetitionsPageNextEventNextEventCircuits(BaseModel):
    updated_on: Optional[Any] = Field(alias="UpdatedOn")
    hash: Optional[str]
    circuit_code: Optional[str] = Field(alias="circuitCode")
    circuit_type_code: Optional[str] = Field(alias="circuitTypeCode")
    circuit_name: Optional[str] = Field(alias="circuitName")
    season: Optional[int]
    circuit_order: Optional[int] = Field(alias="circuitOrder")
    circuit_type_name: Optional[str] = Field(alias="circuitTypeName")


class GetAllCompetitionsGetAllCompetitionsPageNextEventNextEventPage(BaseModel):
    id: Optional[str]
    type_id: Optional[str] = Field(alias="typeId")
    language: Optional[str]
    title: Optional[str]
    competition_id: Optional[str] = Field(alias="competitionId")
    event_id: Optional[int] = Field(alias="eventId")
    site_id: Optional[str] = Field(alias="siteId")
    seo_description: Optional[str] = Field(alias="seoDescription")
    slug: Optional[str]
    published_by_id: Optional[str] = Field(alias="publishedById")
    published_by_name: Optional[str] = Field(alias="publishedByName")
    published: Optional[Any]
    gated_content: Optional[bool] = Field(alias="gatedContent")
    campaign_id: Optional[str] = Field(alias="campaignId")


class GetAllCompetitionsGetAllCompetitionsPageNextEventLastEvent(BaseModel):
    id: Optional[int]
    updated_on: Optional[Any] = Field(alias="updatedOn")
    name: Optional[str]
    start_date: Optional[Any] = Field(alias="startDate")
    end_date: Optional[Any] = Field(alias="endDate")
    hash: Optional[str]
    venue: Optional[str]
    country_code: Optional[str] = Field(alias="countryCode")
    country_name: Optional[str] = Field(alias="countryName")
    area_code: Optional[str] = Field(alias="areaCode")
    area_name: Optional[str] = Field(alias="areaName")
    age_code: Optional[str] = Field(alias="ageCode")
    indoor_outdoor: Optional[str] = Field(alias="indoorOutdoor")
    category_code: Optional[str] = Field(alias="categoryCode")
    category_name: Optional[str] = Field(alias="categoryName")
    category_order: Optional[int] = Field(alias="categoryOrder")
    sub_category_code: Optional[str] = Field(alias="subCategoryCode")
    sub_category_name: Optional[str] = Field(alias="subCategoryName")
    show_web_live_banner: Optional[bool] = Field(alias="showWebLiveBanner")
    sub_category_order: Optional[int] = Field(alias="subCategoryOrder")
    class_code: Optional[str] = Field(alias="classCode")
    class_order: Optional[int] = Field(alias="classOrder")
    is_published: Optional[bool] = Field(alias="isPublished")
    has_comp_doc_results: Optional[bool] = Field(alias="hasCompDocResults")
    name_url_slug: Optional[str] = Field(alias="nameUrlSlug")
    start_date_year: Optional[int] = Field(alias="startDateYear")
    circuits: Optional[
        List[
            Optional[
                "GetAllCompetitionsGetAllCompetitionsPageNextEventLastEventCircuits"
            ]
        ]
    ]
    area_name_url_slug: Optional[str] = Field(alias="areaNameUrlSlug")
    category_name_url_slug: Optional[str] = Field(alias="categoryNameUrlSlug")
    sub_category_name_url_slug: Optional[str] = Field(alias="subCategoryNameUrlSlug")
    discipline_codes: Optional[List[Optional[str]]] = Field(alias="disciplineCodes")
    event_id__w_a: Optional[int] = Field(alias="eventId_WA")
    has_timetable: Optional[bool] = Field(alias="hasTimetable")
    page: Optional["GetAllCompetitionsGetAllCompetitionsPageNextEventLastEventPage"]
    event_start_date_time: Optional[Any] = Field(alias="eventStartDateTime")
    event_end_date_time: Optional[Any] = Field(alias="eventEndDateTime")
    venue_timezone: Optional[str] = Field(alias="venueTimezone")
    banner_lead_time_in_hours: Optional[int] = Field(alias="bannerLeadTimeInHours")


class GetAllCompetitionsGetAllCompetitionsPageNextEventLastEventCircuits(BaseModel):
    updated_on: Optional[Any] = Field(alias="UpdatedOn")
    hash: Optional[str]
    circuit_code: Optional[str] = Field(alias="circuitCode")
    circuit_type_code: Optional[str] = Field(alias="circuitTypeCode")
    circuit_name: Optional[str] = Field(alias="circuitName")
    season: Optional[int]
    circuit_order: Optional[int] = Field(alias="circuitOrder")
    circuit_type_name: Optional[str] = Field(alias="circuitTypeName")


class GetAllCompetitionsGetAllCompetitionsPageNextEventLastEventPage(BaseModel):
    id: Optional[str]
    type_id: Optional[str] = Field(alias="typeId")
    language: Optional[str]
    title: Optional[str]
    competition_id: Optional[str] = Field(alias="competitionId")
    event_id: Optional[int] = Field(alias="eventId")
    site_id: Optional[str] = Field(alias="siteId")
    seo_description: Optional[str] = Field(alias="seoDescription")
    slug: Optional[str]
    published_by_id: Optional[str] = Field(alias="publishedById")
    published_by_name: Optional[str] = Field(alias="publishedByName")
    published: Optional[Any]
    gated_content: Optional[bool] = Field(alias="gatedContent")
    campaign_id: Optional[str] = Field(alias="campaignId")


class GetAllCompetitionsGetAllCompetitionsPageNextEventPage(BaseModel):
    id: Optional[str]
    type_id: Optional[str] = Field(alias="typeId")
    language: Optional[str]
    title: Optional[str]
    competition_id: Optional[str] = Field(alias="competitionId")
    event_id: Optional[int] = Field(alias="eventId")
    event: Optional["GetAllCompetitionsGetAllCompetitionsPageNextEventPageEvent"]
    site_id: Optional[str] = Field(alias="siteId")
    minisite: Optional["GetAllCompetitionsGetAllCompetitionsPageNextEventPageMinisite"]
    seo_description: Optional[str] = Field(alias="seoDescription")
    slug: Optional[str]
    published_by_id: Optional[str] = Field(alias="publishedById")
    published_by_name: Optional[str] = Field(alias="publishedByName")
    published: Optional[Any]
    content_modules: Optional[
        List[
            Optional[
                "GetAllCompetitionsGetAllCompetitionsPageNextEventPageContentModules"
            ]
        ]
    ] = Field(alias="contentModules")
    gated_content: Optional[bool] = Field(alias="gatedContent")
    campaign_id: Optional[str] = Field(alias="campaignId")
    campaign: Optional["GetAllCompetitionsGetAllCompetitionsPageNextEventPageCampaign"]


class GetAllCompetitionsGetAllCompetitionsPageNextEventPageEvent(BaseModel):
    id: Optional[int]
    updated_on: Optional[Any] = Field(alias="updatedOn")
    name: Optional[str]
    start_date: Optional[Any] = Field(alias="startDate")
    end_date: Optional[Any] = Field(alias="endDate")
    hash: Optional[str]
    venue: Optional[str]
    country_code: Optional[str] = Field(alias="countryCode")
    country_name: Optional[str] = Field(alias="countryName")
    area_code: Optional[str] = Field(alias="areaCode")
    area_name: Optional[str] = Field(alias="areaName")
    age_code: Optional[str] = Field(alias="ageCode")
    indoor_outdoor: Optional[str] = Field(alias="indoorOutdoor")
    category_code: Optional[str] = Field(alias="categoryCode")
    category_name: Optional[str] = Field(alias="categoryName")
    category_order: Optional[int] = Field(alias="categoryOrder")
    sub_category_code: Optional[str] = Field(alias="subCategoryCode")
    sub_category_name: Optional[str] = Field(alias="subCategoryName")
    show_web_live_banner: Optional[bool] = Field(alias="showWebLiveBanner")
    sub_category_order: Optional[int] = Field(alias="subCategoryOrder")
    class_code: Optional[str] = Field(alias="classCode")
    class_order: Optional[int] = Field(alias="classOrder")
    is_published: Optional[bool] = Field(alias="isPublished")
    has_comp_doc_results: Optional[bool] = Field(alias="hasCompDocResults")
    name_url_slug: Optional[str] = Field(alias="nameUrlSlug")
    start_date_year: Optional[int] = Field(alias="startDateYear")
    area_name_url_slug: Optional[str] = Field(alias="areaNameUrlSlug")
    category_name_url_slug: Optional[str] = Field(alias="categoryNameUrlSlug")
    sub_category_name_url_slug: Optional[str] = Field(alias="subCategoryNameUrlSlug")
    discipline_codes: Optional[List[Optional[str]]] = Field(alias="disciplineCodes")
    event_id__w_a: Optional[int] = Field(alias="eventId_WA")
    has_timetable: Optional[bool] = Field(alias="hasTimetable")
    event_start_date_time: Optional[Any] = Field(alias="eventStartDateTime")
    event_end_date_time: Optional[Any] = Field(alias="eventEndDateTime")
    venue_timezone: Optional[str] = Field(alias="venueTimezone")
    banner_lead_time_in_hours: Optional[int] = Field(alias="bannerLeadTimeInHours")


class GetAllCompetitionsGetAllCompetitionsPageNextEventPageMinisite(BaseModel):
    id: Optional[str]
    name: Optional[str]
    logo_id: Optional[str] = Field(alias="logoId")
    logo_edited: Optional[str] = Field(alias="logoEdited")
    feature_image_id: Optional[str] = Field(alias="featureImageId")
    feature_image_edited: Optional[str] = Field(alias="featureImageEdited")
    theme: Optional[str]
    default_sponsor_ids: Optional[List[Optional[str]]] = Field(
        alias="defaultSponsorIds"
    )
    sponsor_ids: Optional[List[Optional[str]]] = Field(alias="sponsorIds")
    event_id: Optional[int] = Field(alias="eventId")
    primary_color: Optional[str] = Field(alias="primaryColor")
    secondary_color: Optional[str] = Field(alias="secondaryColor")
    tertiary_color: Optional[str] = Field(alias="tertiaryColor")
    additional_colours: Optional[List[Optional[str]]] = Field(alias="additionalColours")
    language_codes: Optional[List[Optional[str]]] = Field(alias="languageCodes")


class GetAllCompetitionsGetAllCompetitionsPageNextEventPageContentModules(BaseModel):
    module_type: Optional[str] = Field(alias="moduleType")
    language: Optional[str]
    related_article_ids: List[Optional[str]] = Field(alias="relatedArticleIds")
    event_ids: List[Optional[int]] = Field(alias="eventIds")
    related_competitor_ids: List[Optional[int]] = Field(alias="relatedCompetitorIds")
    related_discipline_codes: Optional[List[Optional[str]]] = Field(
        alias="relatedDisciplineCodes"
    )
    athlete_ids: Optional[List[Optional[str]]] = Field(alias="athleteIds")
    media_ids: List[Optional[str]] = Field(alias="mediaIds")
    social_links: Optional[List[Optional[str]]] = Field(alias="socialLinks")
    minisite_id: Optional[str] = Field(alias="minisiteId")
    location_id: Optional[str] = Field(alias="locationId")
    event_id: Optional[int] = Field(alias="eventId")
    tags: Optional[List[Optional[str]]]
    description: Optional[str]
    event_name: Optional[str] = Field(alias="eventName")
    tag_id: Optional[str] = Field(alias="tagId")
    more_news_link: Optional[str] = Field(alias="moreNewsLink")
    more_news_text: Optional[str] = Field(alias="moreNewsText")
    colour: Optional[str]
    image_edited: Optional[str] = Field(alias="imageEdited")
    text_position: Optional[str] = Field(alias="textPosition")
    text_colour: Optional[str] = Field(alias="textColour")
    title: Optional[str]
    top_title: Optional[str] = Field(alias="topTitle")
    bottom_title: Optional[str] = Field(alias="bottomTitle")
    subtitle: Optional[str]
    category: Optional[str]
    standfirst: Optional[str]
    url: Optional[str]
    button_text: Optional[str] = Field(alias="buttonText")
    image_position: Optional[str] = Field(alias="imagePosition")
    background_color: Optional[str] = Field(alias="backgroundColor")
    show_timestamp: Optional[bool] = Field(alias="showTimestamp")
    content: Optional[str]
    parent_id: Optional[str] = Field(alias="parentId")
    event_id_wa: Optional[int] = Field(alias="eventIdWa")
    layout: Optional[int]
    slug: Optional[str]
    video_ids: Optional[List[Optional[str]]] = Field(alias="videoIds")
    video_playlist_id: Optional[str] = Field(alias="videoPlaylistId")
    video_id: Optional[str] = Field(alias="videoId")


class GetAllCompetitionsGetAllCompetitionsPageNextEventPageCampaign(BaseModel):
    id: Optional[str]
    name: Optional[str]
    tag: Optional[str]
    type: Optional[str]
    description: Optional[str]
    thank_you_message: Optional[str] = Field(alias="thankYouMessage")
    already_signed_message: Optional[str] = Field(alias="alreadySignedMessage")
    close_date: Optional[Any] = Field(alias="closeDate")
    redirect_url: Optional[str] = Field(alias="redirectUrl")
    tag_user_friendly_name: Optional[str] = Field(alias="tagUserFriendlyName")
    background_image_edited: Optional[str] = Field(alias="backgroundImageEdited")
    header_image_edited: Optional[str] = Field(alias="headerImageEdited")
    visible_on_preference_center: Optional[bool] = Field(
        alias="visibleOnPreferenceCenter"
    )
    short_form: Optional[bool] = Field(alias="shortForm")
    top_level_bucket_id: Optional[str] = Field(alias="topLevelBucketId")


class GetAllCompetitionsGetAllCompetitionsAllEvents(BaseModel):
    id: Optional[str]
    name: Optional[str]
    circuit_type_code: Optional[str] = Field(alias="circuitTypeCode")
    event_sub_category_code: Optional[str] = Field(alias="eventSubCategoryCode")
    description: Optional[str]
    circuit_code: Optional[str] = Field(alias="circuitCode")
    url_slug: Optional[str] = Field(alias="urlSlug")
    order: Optional[int]
    category: Optional[int]
    about: Optional[str]
    primary_media_id: Optional[str] = Field(alias="primaryMediaId")
    related_media_ids: Optional[List[Optional[str]]] = Field(alias="relatedMediaIds")
    logo_light_id: Optional[str] = Field(alias="logoLightId")
    logo_dark_id: Optional[str] = Field(alias="logoDarkId")
    style_overrides: Optional[str] = Field(alias="styleOverrides")
    related_info: Optional[List[Optional[str]]] = Field(alias="relatedInfo")
    next_event: Optional["GetAllCompetitionsGetAllCompetitionsAllEventsNextEvent"] = (
        Field(alias="nextEvent")
    )
    last_event: Optional["GetAllCompetitionsGetAllCompetitionsAllEventsLastEvent"] = (
        Field(alias="lastEvent")
    )
    next_event_start_date: Optional[Any] = Field(alias="nextEventStartDate")
    page_id: Optional[str] = Field(alias="pageId")
    page: Optional["GetAllCompetitionsGetAllCompetitionsAllEventsPage"]


class GetAllCompetitionsGetAllCompetitionsAllEventsNextEvent(BaseModel):
    id: Optional[int]
    updated_on: Optional[Any] = Field(alias="updatedOn")
    name: Optional[str]
    start_date: Optional[Any] = Field(alias="startDate")
    end_date: Optional[Any] = Field(alias="endDate")
    hash: Optional[str]
    venue: Optional[str]
    country_code: Optional[str] = Field(alias="countryCode")
    country_name: Optional[str] = Field(alias="countryName")
    area_code: Optional[str] = Field(alias="areaCode")
    area_name: Optional[str] = Field(alias="areaName")
    age_code: Optional[str] = Field(alias="ageCode")
    indoor_outdoor: Optional[str] = Field(alias="indoorOutdoor")
    category_code: Optional[str] = Field(alias="categoryCode")
    category_name: Optional[str] = Field(alias="categoryName")
    category_order: Optional[int] = Field(alias="categoryOrder")
    sub_category_code: Optional[str] = Field(alias="subCategoryCode")
    sub_category_name: Optional[str] = Field(alias="subCategoryName")
    show_web_live_banner: Optional[bool] = Field(alias="showWebLiveBanner")
    sub_category_order: Optional[int] = Field(alias="subCategoryOrder")
    class_code: Optional[str] = Field(alias="classCode")
    class_order: Optional[int] = Field(alias="classOrder")
    is_published: Optional[bool] = Field(alias="isPublished")
    has_comp_doc_results: Optional[bool] = Field(alias="hasCompDocResults")
    name_url_slug: Optional[str] = Field(alias="nameUrlSlug")
    start_date_year: Optional[int] = Field(alias="startDateYear")
    circuits: Optional[
        List[Optional["GetAllCompetitionsGetAllCompetitionsAllEventsNextEventCircuits"]]
    ]
    area_name_url_slug: Optional[str] = Field(alias="areaNameUrlSlug")
    category_name_url_slug: Optional[str] = Field(alias="categoryNameUrlSlug")
    sub_category_name_url_slug: Optional[str] = Field(alias="subCategoryNameUrlSlug")
    discipline_codes: Optional[List[Optional[str]]] = Field(alias="disciplineCodes")
    event_id__w_a: Optional[int] = Field(alias="eventId_WA")
    has_timetable: Optional[bool] = Field(alias="hasTimetable")
    page: Optional["GetAllCompetitionsGetAllCompetitionsAllEventsNextEventPage"]
    event_start_date_time: Optional[Any] = Field(alias="eventStartDateTime")
    event_end_date_time: Optional[Any] = Field(alias="eventEndDateTime")
    venue_timezone: Optional[str] = Field(alias="venueTimezone")
    banner_lead_time_in_hours: Optional[int] = Field(alias="bannerLeadTimeInHours")


class GetAllCompetitionsGetAllCompetitionsAllEventsNextEventCircuits(BaseModel):
    updated_on: Optional[Any] = Field(alias="UpdatedOn")
    hash: Optional[str]
    circuit_code: Optional[str] = Field(alias="circuitCode")
    circuit_type_code: Optional[str] = Field(alias="circuitTypeCode")
    circuit_name: Optional[str] = Field(alias="circuitName")
    season: Optional[int]
    circuit_order: Optional[int] = Field(alias="circuitOrder")
    circuit_type_name: Optional[str] = Field(alias="circuitTypeName")


class GetAllCompetitionsGetAllCompetitionsAllEventsNextEventPage(BaseModel):
    id: Optional[str]
    type_id: Optional[str] = Field(alias="typeId")
    language: Optional[str]
    title: Optional[str]
    competition_id: Optional[str] = Field(alias="competitionId")
    event_id: Optional[int] = Field(alias="eventId")
    site_id: Optional[str] = Field(alias="siteId")
    seo_description: Optional[str] = Field(alias="seoDescription")
    slug: Optional[str]
    published_by_id: Optional[str] = Field(alias="publishedById")
    published_by_name: Optional[str] = Field(alias="publishedByName")
    published: Optional[Any]
    gated_content: Optional[bool] = Field(alias="gatedContent")
    campaign_id: Optional[str] = Field(alias="campaignId")


class GetAllCompetitionsGetAllCompetitionsAllEventsLastEvent(BaseModel):
    id: Optional[int]
    updated_on: Optional[Any] = Field(alias="updatedOn")
    name: Optional[str]
    start_date: Optional[Any] = Field(alias="startDate")
    end_date: Optional[Any] = Field(alias="endDate")
    hash: Optional[str]
    venue: Optional[str]
    country_code: Optional[str] = Field(alias="countryCode")
    country_name: Optional[str] = Field(alias="countryName")
    area_code: Optional[str] = Field(alias="areaCode")
    area_name: Optional[str] = Field(alias="areaName")
    age_code: Optional[str] = Field(alias="ageCode")
    indoor_outdoor: Optional[str] = Field(alias="indoorOutdoor")
    category_code: Optional[str] = Field(alias="categoryCode")
    category_name: Optional[str] = Field(alias="categoryName")
    category_order: Optional[int] = Field(alias="categoryOrder")
    sub_category_code: Optional[str] = Field(alias="subCategoryCode")
    sub_category_name: Optional[str] = Field(alias="subCategoryName")
    show_web_live_banner: Optional[bool] = Field(alias="showWebLiveBanner")
    sub_category_order: Optional[int] = Field(alias="subCategoryOrder")
    class_code: Optional[str] = Field(alias="classCode")
    class_order: Optional[int] = Field(alias="classOrder")
    is_published: Optional[bool] = Field(alias="isPublished")
    has_comp_doc_results: Optional[bool] = Field(alias="hasCompDocResults")
    name_url_slug: Optional[str] = Field(alias="nameUrlSlug")
    start_date_year: Optional[int] = Field(alias="startDateYear")
    circuits: Optional[
        List[Optional["GetAllCompetitionsGetAllCompetitionsAllEventsLastEventCircuits"]]
    ]
    area_name_url_slug: Optional[str] = Field(alias="areaNameUrlSlug")
    category_name_url_slug: Optional[str] = Field(alias="categoryNameUrlSlug")
    sub_category_name_url_slug: Optional[str] = Field(alias="subCategoryNameUrlSlug")
    discipline_codes: Optional[List[Optional[str]]] = Field(alias="disciplineCodes")
    event_id__w_a: Optional[int] = Field(alias="eventId_WA")
    has_timetable: Optional[bool] = Field(alias="hasTimetable")
    page: Optional["GetAllCompetitionsGetAllCompetitionsAllEventsLastEventPage"]
    event_start_date_time: Optional[Any] = Field(alias="eventStartDateTime")
    event_end_date_time: Optional[Any] = Field(alias="eventEndDateTime")
    venue_timezone: Optional[str] = Field(alias="venueTimezone")
    banner_lead_time_in_hours: Optional[int] = Field(alias="bannerLeadTimeInHours")


class GetAllCompetitionsGetAllCompetitionsAllEventsLastEventCircuits(BaseModel):
    updated_on: Optional[Any] = Field(alias="UpdatedOn")
    hash: Optional[str]
    circuit_code: Optional[str] = Field(alias="circuitCode")
    circuit_type_code: Optional[str] = Field(alias="circuitTypeCode")
    circuit_name: Optional[str] = Field(alias="circuitName")
    season: Optional[int]
    circuit_order: Optional[int] = Field(alias="circuitOrder")
    circuit_type_name: Optional[str] = Field(alias="circuitTypeName")


class GetAllCompetitionsGetAllCompetitionsAllEventsLastEventPage(BaseModel):
    id: Optional[str]
    type_id: Optional[str] = Field(alias="typeId")
    language: Optional[str]
    title: Optional[str]
    competition_id: Optional[str] = Field(alias="competitionId")
    event_id: Optional[int] = Field(alias="eventId")
    site_id: Optional[str] = Field(alias="siteId")
    seo_description: Optional[str] = Field(alias="seoDescription")
    slug: Optional[str]
    published_by_id: Optional[str] = Field(alias="publishedById")
    published_by_name: Optional[str] = Field(alias="publishedByName")
    published: Optional[Any]
    gated_content: Optional[bool] = Field(alias="gatedContent")
    campaign_id: Optional[str] = Field(alias="campaignId")


class GetAllCompetitionsGetAllCompetitionsAllEventsPage(BaseModel):
    id: Optional[str]
    type_id: Optional[str] = Field(alias="typeId")
    language: Optional[str]
    title: Optional[str]
    competition_id: Optional[str] = Field(alias="competitionId")
    event_id: Optional[int] = Field(alias="eventId")
    event: Optional["GetAllCompetitionsGetAllCompetitionsAllEventsPageEvent"]
    site_id: Optional[str] = Field(alias="siteId")
    minisite: Optional["GetAllCompetitionsGetAllCompetitionsAllEventsPageMinisite"]
    seo_description: Optional[str] = Field(alias="seoDescription")
    slug: Optional[str]
    published_by_id: Optional[str] = Field(alias="publishedById")
    published_by_name: Optional[str] = Field(alias="publishedByName")
    published: Optional[Any]
    content_modules: Optional[
        List[
            Optional["GetAllCompetitionsGetAllCompetitionsAllEventsPageContentModules"]
        ]
    ] = Field(alias="contentModules")
    gated_content: Optional[bool] = Field(alias="gatedContent")
    campaign_id: Optional[str] = Field(alias="campaignId")
    campaign: Optional["GetAllCompetitionsGetAllCompetitionsAllEventsPageCampaign"]


class GetAllCompetitionsGetAllCompetitionsAllEventsPageEvent(BaseModel):
    id: Optional[int]
    updated_on: Optional[Any] = Field(alias="updatedOn")
    name: Optional[str]
    start_date: Optional[Any] = Field(alias="startDate")
    end_date: Optional[Any] = Field(alias="endDate")
    hash: Optional[str]
    venue: Optional[str]
    country_code: Optional[str] = Field(alias="countryCode")
    country_name: Optional[str] = Field(alias="countryName")
    area_code: Optional[str] = Field(alias="areaCode")
    area_name: Optional[str] = Field(alias="areaName")
    age_code: Optional[str] = Field(alias="ageCode")
    indoor_outdoor: Optional[str] = Field(alias="indoorOutdoor")
    category_code: Optional[str] = Field(alias="categoryCode")
    category_name: Optional[str] = Field(alias="categoryName")
    category_order: Optional[int] = Field(alias="categoryOrder")
    sub_category_code: Optional[str] = Field(alias="subCategoryCode")
    sub_category_name: Optional[str] = Field(alias="subCategoryName")
    show_web_live_banner: Optional[bool] = Field(alias="showWebLiveBanner")
    sub_category_order: Optional[int] = Field(alias="subCategoryOrder")
    class_code: Optional[str] = Field(alias="classCode")
    class_order: Optional[int] = Field(alias="classOrder")
    is_published: Optional[bool] = Field(alias="isPublished")
    has_comp_doc_results: Optional[bool] = Field(alias="hasCompDocResults")
    name_url_slug: Optional[str] = Field(alias="nameUrlSlug")
    start_date_year: Optional[int] = Field(alias="startDateYear")
    area_name_url_slug: Optional[str] = Field(alias="areaNameUrlSlug")
    category_name_url_slug: Optional[str] = Field(alias="categoryNameUrlSlug")
    sub_category_name_url_slug: Optional[str] = Field(alias="subCategoryNameUrlSlug")
    discipline_codes: Optional[List[Optional[str]]] = Field(alias="disciplineCodes")
    event_id__w_a: Optional[int] = Field(alias="eventId_WA")
    has_timetable: Optional[bool] = Field(alias="hasTimetable")
    event_start_date_time: Optional[Any] = Field(alias="eventStartDateTime")
    event_end_date_time: Optional[Any] = Field(alias="eventEndDateTime")
    venue_timezone: Optional[str] = Field(alias="venueTimezone")
    banner_lead_time_in_hours: Optional[int] = Field(alias="bannerLeadTimeInHours")


class GetAllCompetitionsGetAllCompetitionsAllEventsPageMinisite(BaseModel):
    id: Optional[str]
    name: Optional[str]
    logo_id: Optional[str] = Field(alias="logoId")
    logo_edited: Optional[str] = Field(alias="logoEdited")
    feature_image_id: Optional[str] = Field(alias="featureImageId")
    feature_image_edited: Optional[str] = Field(alias="featureImageEdited")
    theme: Optional[str]
    default_sponsor_ids: Optional[List[Optional[str]]] = Field(
        alias="defaultSponsorIds"
    )
    sponsor_ids: Optional[List[Optional[str]]] = Field(alias="sponsorIds")
    event_id: Optional[int] = Field(alias="eventId")
    primary_color: Optional[str] = Field(alias="primaryColor")
    secondary_color: Optional[str] = Field(alias="secondaryColor")
    tertiary_color: Optional[str] = Field(alias="tertiaryColor")
    additional_colours: Optional[List[Optional[str]]] = Field(alias="additionalColours")
    language_codes: Optional[List[Optional[str]]] = Field(alias="languageCodes")


class GetAllCompetitionsGetAllCompetitionsAllEventsPageContentModules(BaseModel):
    module_type: Optional[str] = Field(alias="moduleType")
    language: Optional[str]
    related_article_ids: List[Optional[str]] = Field(alias="relatedArticleIds")
    event_ids: List[Optional[int]] = Field(alias="eventIds")
    related_competitor_ids: List[Optional[int]] = Field(alias="relatedCompetitorIds")
    related_discipline_codes: Optional[List[Optional[str]]] = Field(
        alias="relatedDisciplineCodes"
    )
    athlete_ids: Optional[List[Optional[str]]] = Field(alias="athleteIds")
    media_ids: List[Optional[str]] = Field(alias="mediaIds")
    social_links: Optional[List[Optional[str]]] = Field(alias="socialLinks")
    minisite_id: Optional[str] = Field(alias="minisiteId")
    location_id: Optional[str] = Field(alias="locationId")
    event_id: Optional[int] = Field(alias="eventId")
    tags: Optional[List[Optional[str]]]
    description: Optional[str]
    event_name: Optional[str] = Field(alias="eventName")
    tag_id: Optional[str] = Field(alias="tagId")
    more_news_link: Optional[str] = Field(alias="moreNewsLink")
    more_news_text: Optional[str] = Field(alias="moreNewsText")
    colour: Optional[str]
    image_edited: Optional[str] = Field(alias="imageEdited")
    text_position: Optional[str] = Field(alias="textPosition")
    text_colour: Optional[str] = Field(alias="textColour")
    title: Optional[str]
    top_title: Optional[str] = Field(alias="topTitle")
    bottom_title: Optional[str] = Field(alias="bottomTitle")
    subtitle: Optional[str]
    category: Optional[str]
    standfirst: Optional[str]
    url: Optional[str]
    button_text: Optional[str] = Field(alias="buttonText")
    image_position: Optional[str] = Field(alias="imagePosition")
    background_color: Optional[str] = Field(alias="backgroundColor")
    show_timestamp: Optional[bool] = Field(alias="showTimestamp")
    content: Optional[str]
    parent_id: Optional[str] = Field(alias="parentId")
    event_id_wa: Optional[int] = Field(alias="eventIdWa")
    layout: Optional[int]
    slug: Optional[str]
    video_ids: Optional[List[Optional[str]]] = Field(alias="videoIds")
    video_playlist_id: Optional[str] = Field(alias="videoPlaylistId")
    video_id: Optional[str] = Field(alias="videoId")


class GetAllCompetitionsGetAllCompetitionsAllEventsPageCampaign(BaseModel):
    id: Optional[str]
    name: Optional[str]
    tag: Optional[str]
    type: Optional[str]
    description: Optional[str]
    thank_you_message: Optional[str] = Field(alias="thankYouMessage")
    already_signed_message: Optional[str] = Field(alias="alreadySignedMessage")
    close_date: Optional[Any] = Field(alias="closeDate")
    redirect_url: Optional[str] = Field(alias="redirectUrl")
    tag_user_friendly_name: Optional[str] = Field(alias="tagUserFriendlyName")
    background_image_edited: Optional[str] = Field(alias="backgroundImageEdited")
    header_image_edited: Optional[str] = Field(alias="headerImageEdited")
    visible_on_preference_center: Optional[bool] = Field(
        alias="visibleOnPreferenceCenter"
    )
    short_form: Optional[bool] = Field(alias="shortForm")
    top_level_bucket_id: Optional[str] = Field(alias="topLevelBucketId")


GetAllCompetitions.update_forward_refs()
GetAllCompetitionsGetAllCompetitions.update_forward_refs()
GetAllCompetitionsGetAllCompetitionsPageNextEvent.update_forward_refs()
GetAllCompetitionsGetAllCompetitionsPageNextEventNextEvent.update_forward_refs()
GetAllCompetitionsGetAllCompetitionsPageNextEventNextEventCircuits.update_forward_refs()
GetAllCompetitionsGetAllCompetitionsPageNextEventNextEventPage.update_forward_refs()
GetAllCompetitionsGetAllCompetitionsPageNextEventLastEvent.update_forward_refs()
GetAllCompetitionsGetAllCompetitionsPageNextEventLastEventCircuits.update_forward_refs()
GetAllCompetitionsGetAllCompetitionsPageNextEventLastEventPage.update_forward_refs()
GetAllCompetitionsGetAllCompetitionsPageNextEventPage.update_forward_refs()
GetAllCompetitionsGetAllCompetitionsPageNextEventPageEvent.update_forward_refs()
GetAllCompetitionsGetAllCompetitionsPageNextEventPageMinisite.update_forward_refs()
GetAllCompetitionsGetAllCompetitionsPageNextEventPageContentModules.update_forward_refs()
GetAllCompetitionsGetAllCompetitionsPageNextEventPageCampaign.update_forward_refs()
GetAllCompetitionsGetAllCompetitionsAllEvents.update_forward_refs()
GetAllCompetitionsGetAllCompetitionsAllEventsNextEvent.update_forward_refs()
GetAllCompetitionsGetAllCompetitionsAllEventsNextEventCircuits.update_forward_refs()
GetAllCompetitionsGetAllCompetitionsAllEventsNextEventPage.update_forward_refs()
GetAllCompetitionsGetAllCompetitionsAllEventsLastEvent.update_forward_refs()
GetAllCompetitionsGetAllCompetitionsAllEventsLastEventCircuits.update_forward_refs()
GetAllCompetitionsGetAllCompetitionsAllEventsLastEventPage.update_forward_refs()
GetAllCompetitionsGetAllCompetitionsAllEventsPage.update_forward_refs()
GetAllCompetitionsGetAllCompetitionsAllEventsPageEvent.update_forward_refs()
GetAllCompetitionsGetAllCompetitionsAllEventsPageMinisite.update_forward_refs()
GetAllCompetitionsGetAllCompetitionsAllEventsPageContentModules.update_forward_refs()
GetAllCompetitionsGetAllCompetitionsAllEventsPageCampaign.update_forward_refs()
