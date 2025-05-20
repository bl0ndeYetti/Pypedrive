from typing import Optional, List, Dict, Any, Union
from enum import Enum
from pydantic import BaseModel, Field
from .common import MonetaryValue # Removed BaseCustomFieldsModel


class DealStatusEnum(str, Enum):
    """Allowed deal status values."""

    open = "open"
    won = "won"
    lost = "lost"
    deleted = "deleted"


class SortDirectionEnum(str, Enum):
    """Allowed sorting directions."""

    asc = "asc"
    desc = "desc"

class DealCreateModel(BaseModel):
    title: str
    value: Optional[Union[float, MonetaryValue, str]] = None  # Can be float, structured, or string "0"
    currency: Optional[str] = None  # Required if value is float/str
    owner_id: Optional[int] = None  # Renamed from user_id
    person_id: Optional[int] = None
    org_id: Optional[int] = None
    pipeline_id: Optional[int] = None
    stage_id: Optional[int] = None
    status: Optional[DealStatusEnum] = Field(
        None,
        description="The status of the deal"
    )
    probability: Optional[float] = None
    lost_reason: Optional[str] = None
    add_time: Optional[str] = None  # YYYY-MM-DD HH:MM:SS or RFC3339
    update_time: Optional[str] = Field(
        None,
        description="The last updated date and time of the deal"
    )
    stage_change_time: Optional[str] = Field(
        None,
        description="The last updated date and time of the deal stage"
    )
    expected_close_date: Optional[str] = None  # YYYY-MM-DD
    visible_to: Optional[int] = None  # 1, 3, 5, 7
    close_time: Optional[str] = Field(
        None,
        description="The date and time of closing the deal. Can only be set if deal status is won or lost."
    )
    won_time: Optional[str] = Field(
        None,
        description="The date and time of changing the deal status as won. Can only be set if deal status is won."
    )
    lost_time: Optional[str] = Field(
        None,
        description="The date and time of changing the deal status as lost. Can only be set if deal status is lost."
    )
    label_ids: Optional[List[int]] = None
    origin: Optional[str] = Field(
        None,
        description="The way this Deal was created. `origin` field is set by Pipedrive when Deal is created and cannot be changed."
    )
    origin_id: Optional[str] = Field(
        None,
        description="The optional ID to further distinguish the origin of the deal - e.g. Which API integration created this Deal."
    )
    channel: Optional[int] = Field(
        None,
        description="The ID of your Marketing channel this Deal was created from."
    )
    channel_id: Optional[str] = Field(
        None,
        description="The optional ID to further distinguish the Marketing channel."
    )
    arr: Optional[float] = Field(
        None,
        description="The Annual Recurring Revenue of the deal"
    )
    mrr: Optional[float] = Field(
        None,
        description="The Monthly Recurring Revenue of the deal"
    )
    acv: Optional[float] = Field(
        None,
        description="The Annual Contract Value of the deal"
    )
    custom_fields: Optional[Dict[str, Any]] = None  # V2 structure

    class Config:
        extra = 'allow' # Allow custom fields not explicitly defined if not using BaseCustomFieldsModel approach

class DealUpdateModel(BaseModel):
    title: Optional[str] = None
    value: Optional[Union[float, MonetaryValue, str]] = None
    currency: Optional[str] = None
    owner_id: Optional[int] = None
    person_id: Optional[int] = None
    org_id: Optional[int] = None
    pipeline_id: Optional[int] = None
    stage_id: Optional[int] = None
    status: Optional[DealStatusEnum] = Field(
        None,
        description="The status of the deal"
    )
    probability: Optional[float] = None
    lost_reason: Optional[str] = None
    add_time: Optional[str] = None
    update_time: Optional[str] = Field(
        None,
        description="The last updated date and time of the deal"
    )
    stage_change_time: Optional[str] = Field(
        None,
        description="The last updated date and time of the deal stage"
    )
    expected_close_date: Optional[str] = None  # YYYY-MM-DD
    visible_to: Optional[int] = None  # 1, 3, 5, 7
    close_time: Optional[str] = Field(
        None,
        description="The date and time of closing the deal. Can only be set if deal status is won or lost."
    )
    won_time: Optional[str] = Field(
        None,
        description="The date and time of changing the deal status as won. Can only be set if deal status is won."
    )
    lost_time: Optional[str] = Field(
        None,
        description="The date and time of changing the deal status as lost. Can only be set if deal status is lost."
    )
    label_ids: Optional[List[int]] = None
    origin: Optional[str] = Field(
        None,
        description="The way this Deal was created. `origin` field is set by Pipedrive when Deal is created and cannot be changed."
    )
    origin_id: Optional[str] = Field(
        None,
        description="The optional ID to further distinguish the origin of the deal - e.g. Which API integration created this Deal."
    )
    channel: Optional[int] = Field(
        None,
        description="The ID of your Marketing channel this Deal was created from."
    )
    channel_id: Optional[str] = Field(
        None,
        description="The optional ID to further distinguish the Marketing channel."
    )
    arr: Optional[float] = Field(
        None,
        description="The Annual Recurring Revenue of the deal"
    )
    mrr: Optional[float] = Field(
        None,
        description="The Monthly Recurring Revenue of the deal"
    )
    acv: Optional[float] = Field(
        None,
        description="The Annual Contract Value of the deal"
    )
    custom_fields: Optional[Dict[str, Any]] = None  # V2 structure

    class Config:
        extra = 'allow'


class GetDealsParams(BaseModel):
    """Query parameters for GET /v2/deals"""

    filter_id: Optional[int] = Field(
        None, description="Only deals matching the given filter are returned"
    )
    ids: Optional[str] = Field(
        None,
        description="Comma separated list of deal IDs to fetch"
    )
    owner_id: Optional[int] = Field(
        None, description="Only deals owned by the given user are returned"
    )
    person_id: Optional[int] = Field(
        None, description="Only deals linked to the given person are returned"
    )
    org_id: Optional[int] = Field(
        None, description="Only deals linked to the given organization are returned"
    )
    pipeline_id: Optional[int] = Field(
        None, description="Only deals in the given pipeline are returned"
    )
    stage_id: Optional[int] = Field(
        None, description="Only deals in the given stage are returned"
    )
    status: Optional[DealStatusEnum] = Field(
        None,
        description="Only fetch deals with a specific status"
    )
    updated_since: Optional[str] = Field(
        None,
        description="Return deals updated after this time (RFC3339)"
    )
    updated_until: Optional[str] = Field(
        None,
        description="Return deals updated before this time (RFC3339)"
    )
    sort_by: Optional[str] = Field(
        None,
        description="Field to sort by, e.g. 'id', 'update_time', 'add_time'"
    )
    sort_direction: Optional[SortDirectionEnum] = Field(
        None, description="The sorting direction"
    )
    include_fields: Optional[str] = Field(
        None,
        description="Additional fields to include in the results"
    )
    custom_fields: Optional[str] = Field(
        None,
        description="Custom field keys to include (comma separated)"
    )
    limit: Optional[int] = Field(
        None, description="Items shown per page (max 500)"
    )
    cursor: Optional[str] = Field(
        None, description="Pagination cursor for the next page"
    )


class GetDealParams(BaseModel):
    """Query parameters for GET /v2/deals/{id}"""

    include_fields: Optional[str] = Field(
        None,
        description="Additional fields to include in the response"
    )
    custom_fields: Optional[str] = Field(
        None,
        description="Custom field keys to include (comma separated)"
    )

