from typing import Optional
from pydantic import BaseModel, Field

class GetNotesParams(BaseModel):
    """Query parameters for GET /v1/notes"""

    user_id: Optional[int] = Field(None, description="Filter by user ID")
    lead_id: Optional[str] = Field(None, description="Filter by lead ID")
    deal_id: Optional[int] = Field(None, description="Filter by deal ID")
    person_id: Optional[int] = Field(None, description="Filter by person ID")
    org_id: Optional[int] = Field(None, description="Filter by organization ID")
    project_id: Optional[int] = Field(None, description="Filter by project ID")
    start: Optional[int] = Field(None, description="Pagination start")
    limit: Optional[int] = Field(None, description="Items per page")
    sort: Optional[str] = Field(
        None,
        description="Field names and sorting mode, e.g. 'add_time DESC'",
    )
    start_date: Optional[str] = Field(None, description="Filter notes from date")
    end_date: Optional[str] = Field(None, description="Filter notes until date")
    pinned_to_lead_flag: Optional[int] = Field(
        None, description="Filter by note to lead pinning state"
    )
    pinned_to_deal_flag: Optional[int] = Field(
        None, description="Filter by note to deal pinning state"
    )
    pinned_to_organization_flag: Optional[int] = Field(
        None, description="Filter by note to organization pinning state"
    )
    pinned_to_person_flag: Optional[int] = Field(
        None, description="Filter by note to person pinning state"
    )
    pinned_to_project_flag: Optional[int] = Field(
        None, description="Filter by note to project pinning state"
    )

class NoteCreateModel(BaseModel):
    """Body parameters for POST /v1/notes"""

    content: str = Field(..., description="Content of the note in HTML")
    lead_id: Optional[str] = Field(
        None, description="ID of the lead the note is attached to"
    )
    deal_id: Optional[int] = Field(
        None, description="ID of the deal the note is attached to"
    )
    person_id: Optional[int] = Field(
        None, description="ID of the person the note is attached to"
    )
    org_id: Optional[int] = Field(
        None, description="ID of the organization the note is attached to"
    )
    project_id: Optional[int] = Field(
        None, description="ID of the project the note is attached to"
    )
    user_id: Optional[int] = Field(
        None, description="ID of the user marked as author"
    )
    add_time: Optional[str] = Field(
        None, description="Optional creation time YYYY-MM-DD HH:MM:SS"
    )
    pinned_to_lead_flag: Optional[int] = None
    pinned_to_deal_flag: Optional[int] = None
    pinned_to_organization_flag: Optional[int] = None
    pinned_to_person_flag: Optional[int] = None
    pinned_to_project_flag: Optional[int] = None

class NoteUpdateModel(BaseModel):
    """Body parameters for PUT /v1/notes/{id}"""

    content: Optional[str] = None
    lead_id: Optional[str] = None
    deal_id: Optional[int] = None
    person_id: Optional[int] = None
    org_id: Optional[int] = None
    project_id: Optional[int] = None
    user_id: Optional[int] = None
    add_time: Optional[str] = None
    pinned_to_lead_flag: Optional[int] = None
    pinned_to_deal_flag: Optional[int] = None
    pinned_to_organization_flag: Optional[int] = None
    pinned_to_person_flag: Optional[int] = None
    pinned_to_project_flag: Optional[int] = None

class CommentCreateModel(BaseModel):
    """Body parameters for POST /v1/notes/{id}/comments"""

    content: str = Field(..., description="Content of the comment in HTML")

class CommentUpdateModel(BaseModel):
    """Body parameters for PUT /v1/notes/{id}/comments/{commentId}"""

    content: str = Field(..., description="Content of the comment in HTML")
