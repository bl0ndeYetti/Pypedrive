from typing import Optional, List, Dict, Any, Union
from pydantic import BaseModel, Field
from .common import MonetaryValue # Removed BaseCustomFieldsModel

class DealCreateModel(BaseModel):
    title: str
    value: Optional[Union[float, MonetaryValue, str]] = None # Can be float, structured, or string "0"
    currency: Optional[str] = None # Required if value is float/str
    owner_id: Optional[int] = None # Renamed from user_id
    person_id: Optional[int] = None
    org_id: Optional[int] = None
    pipeline_id: Optional[int] = None
    stage_id: Optional[int] = None
    status: Optional[str] = None # 'open', 'won', 'lost'
    probability: Optional[float] = None
    lost_reason: Optional[str] = None
    add_time: Optional[str] = None # YYYY-MM-DD HH:MM:SS or RFC3339
    expected_close_date: Optional[str] = None # YYYY-MM-DD
    visible_to: Optional[int] = None # 1, 3, 5, 7
    label_ids: Optional[List[int]] = None
    custom_fields: Optional[Dict[str, Any]] = None # V2 structure
    # ACV/ARR/MRR fields might be read-only or calculated

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
    status: Optional[str] = None # 'open', 'won', 'lost'
    probability: Optional[float] = None
    lost_reason: Optional[str] = None
    expected_close_date: Optional[str] = None # YYYY-MM-DD
    visible_to: Optional[int] = None # 1, 3, 5, 7
    label_ids: Optional[List[int]] = None
    custom_fields: Optional[Dict[str, Any]] = None # V2 structure
    # ACV/ARR/MRR fields might be read-only or calculated

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
    status: Optional[str] = Field(
        None,
        description="Filter by deal status (open, won, lost, deleted)"
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
    sort_direction: Optional[str] = Field(
        None, description="Sorting direction, asc or desc"
    )
    include_fields: Optional[str] = Field(
        None,
        description="Additional fields to include in the results"
    )
    custom_fields: Optional[str] = Field(
        None,
        description="Custom field keys to include (comma separated)"
    )
    start: Optional[int] = Field(
        None, description="Pagination start offset"
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

