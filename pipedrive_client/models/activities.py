from typing import Optional, List, Dict, Any, Union
from pydantic import BaseModel, Field
from .common import Address, Attendee, Participant, BaseCustomFieldsModel


class ActivityCreateModel(BaseCustomFieldsModel):
    """Body parameters for POST /api/v2/activities."""

    subject: str
    type: Optional[str] = None
    public_description: Optional[str] = None
    note: Optional[str] = None
    due_date: Optional[str] = None  # YYYY-MM-DD
    due_time: Optional[str] = None  # HH:MM
    duration: Optional[str] = None  # HH:MM
    owner_id: Optional[int] = None  # Renamed from user_id
    deal_id: Optional[int] = None
    lead_id: Optional[str] = None
    person_id: Optional[int] = Field(
        None, description="Read-only in v2, set via participants"
    )
    org_id: Optional[int] = None
    project_id: Optional[int] = None
    participants: Optional[List[Participant]] = None
    location: Optional[Union[str, Address]] = None
    busy: Optional[bool] = Field(None, alias="busy_flag")
    attendees: Optional[List[Attendee]] = None
    done: Optional[bool] = None
    priority: Optional[int] = None

    class Config:
        validate_by_name = True


class ActivityUpdateModel(BaseCustomFieldsModel):
    """Body parameters for PATCH /api/v2/activities/{id}."""

    subject: Optional[str] = None
    type: Optional[str] = None
    public_description: Optional[str] = None
    note: Optional[str] = None
    due_date: Optional[str] = None  # YYYY-MM-DD
    due_time: Optional[str] = None  # HH:MM
    duration: Optional[str] = None  # HH:MM
    owner_id: Optional[int] = None  # Renamed from user_id
    deal_id: Optional[int] = None
    lead_id: Optional[str] = None
    person_id: Optional[int] = Field(
        None, description="Read-only in v2, set via participants"
    )
    org_id: Optional[int] = None
    project_id: Optional[int] = None
    participants: Optional[List[Participant]] = None
    location: Optional[Union[str, Address]] = None
    busy: Optional[bool] = Field(None, alias="busy_flag")
    attendees: Optional[List[Attendee]] = None
    done: Optional[bool] = None
    priority: Optional[int] = None

    class Config:
        validate_by_name = True


class GetActivitiesParams(BaseModel):
    """Query parameters for GET /api/v2/activities."""

    filter_id: Optional[int] = Field(
        None,
        description="Only activities matching the specified filter are returned",
    )
    ids: Optional[str] = Field(
        None,
        description="Comma-separated list of up to 100 activity IDs to fetch",
    )
    owner_id: Optional[int] = Field(
        None,
        description="Only activities owned by the specified user are returned",
    )
    deal_id: Optional[int] = Field(
        None, description="Only activities linked to the specified deal"
    )
    lead_id: Optional[str] = Field(
        None, description="Only activities linked to the specified lead"
    )
    person_id: Optional[int] = Field(
        None,
        description="Only activities whose primary participant is the given person",
    )
    org_id: Optional[int] = Field(
        None, description="Only activities linked to the specified organization"
    )
    done: Optional[bool] = Field(
        None, description="Whether the activity is done"
    )
    updated_since: Optional[str] = Field(
        None,
        description="Return activities with update_time >= this time (RFC3339)",
    )
    updated_until: Optional[str] = Field(
        None,
        description="Return activities with update_time < this time (RFC3339)",
    )
    sort_by: Optional[str] = Field(
        None,
        description="Field to sort by: id, update_time, add_time, due_date",
    )
    sort_direction: Optional[str] = Field(
        None, description="Sorting direction, asc or desc"
    )
    include_fields: Optional[str] = Field(
        None, description="Comma separated additional fields to include"
    )
    limit: Optional[int] = Field(
        None, description="Number of items to return (max 500)"
    )
    cursor: Optional[str] = Field(
        None, description="Pagination cursor for next page"
    )


class GetActivityParams(BaseModel):
    """Query parameters for GET /api/v2/activities/{id}."""

    include_fields: Optional[str] = Field(
        None, description="Comma separated additional fields to include"
    )
