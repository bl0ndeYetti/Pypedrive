from typing import Optional, List
from pydantic import BaseModel, Field
from .common import MonetaryValue

class GetLeadsParams(BaseModel):
    """Query parameters for GET /v1/leads"""

    limit: Optional[int] = Field(None, description="Items per page")
    start: Optional[int] = Field(None, description="Pagination start position")
    owner_id: Optional[int] = Field(None, description="Filter by owner user ID")
    person_id: Optional[int] = Field(None, description="Filter by person ID")
    organization_id: Optional[int] = Field(
        None, description="Filter by organization ID"
    )
    filter_id: Optional[int] = Field(None, description="ID of the filter to use")
    sort: Optional[str] = Field(
        None,
        description="Field name and sorting mode, e.g. 'add_time DESC'",
    )

class LeadValue(MonetaryValue):
    """Potential value of the lead."""

class LeadCreateModel(BaseModel):
    """Body parameters for POST /v1/leads"""

    title: str = Field(..., description="Name of the lead")
    owner_id: Optional[int] = Field(
        None,
        description="ID of the user that will own the lead",
    )
    label_ids: Optional[List[int]] = Field(
        None, description="IDs of labels associated with the lead"
    )
    person_id: Optional[int] = Field(
        None, description="ID of a person linked to the lead"
    )
    organization_id: Optional[int] = Field(
        None, description="ID of an organization linked to the lead"
    )
    value: Optional[LeadValue] = Field(
        None, description="Potential value of the lead"
    )
    expected_close_date: Optional[str] = Field(
        None, description="Expected close date YYYY-MM-DD"
    )
    visible_to: Optional[int] = Field(
        None, description="Visibility of the lead"
    )
    was_seen: Optional[bool] = Field(
        None, description="Flag indicating whether the lead was seen"
    )
    origin_id: Optional[str] = Field(
        None, description="Optional ID to distinguish the origin of the lead"
    )
    channel: Optional[int] = Field(
        None, description="Marketing channel ID"
    )
    channel_id: Optional[str] = Field(
        None, description="Optional ID to distinguish the channel"
    )

class LeadUpdateModel(BaseModel):
    """Body parameters for PATCH /v1/leads/{id}"""

    title: Optional[str] = None
    owner_id: Optional[int] = None
    label_ids: Optional[List[int]] = None
    person_id: Optional[int] = None
    organization_id: Optional[int] = None
    is_archived: Optional[bool] = None
    value: Optional[LeadValue] = None
    expected_close_date: Optional[str] = None
    visible_to: Optional[int] = None
    was_seen: Optional[bool] = None
    channel: Optional[int] = None
    channel_id: Optional[str] = None
    origin_id: Optional[str] = None

class ConvertLeadToDealBody(BaseModel):
    """Body parameters for POST /api/v2/leads/{id}/convert/deal"""

    stage_id: Optional[int] = Field(
        None, description="ID of the stage the created deal will be added to"
    )
    pipeline_id: Optional[int] = Field(
        None,
        description="ID of the pipeline the created deal will belong to",
    )

class SearchLeadsParams(BaseModel):
    """Query parameters for GET /v1/leads/search"""

    term: str = Field(..., description="Search term")
    person_id: Optional[int] = Field(None, description="Filter by person ID")
    organization_id: Optional[int] = Field(
        None, description="Filter by organization ID"
    )
    limit: Optional[int] = Field(None, description="Items per page")
    start: Optional[int] = Field(None, description="Pagination start position")
