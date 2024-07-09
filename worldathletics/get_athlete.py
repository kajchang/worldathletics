# Generated by ariadne-codegen on 2024-06-04 14:46
# Source: graphql/queries.graphql

from typing import Any, List, Optional

from pydantic import Field

from .base_model import BaseModel


class GetAthlete(BaseModel):
    get_athlete: Optional["GetAthleteGetAthlete"] = Field(alias="getAthlete")


class GetAthleteGetAthlete(BaseModel):
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
    primary_media: Optional[List[Optional["GetAthleteGetAthletePrimaryMedia"]]] = Field(
        alias="primaryMedia"
    )
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


class GetAthleteGetAthletePrimaryMedia(BaseModel):
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


GetAthlete.update_forward_refs()
GetAthleteGetAthlete.update_forward_refs()
GetAthleteGetAthletePrimaryMedia.update_forward_refs()
