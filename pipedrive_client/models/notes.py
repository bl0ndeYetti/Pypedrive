from typing import Optional
from pydantic import BaseModel, Field


class GetNotesParams(BaseModel):
    """Query parameters for GET /v1/notes."""

    user_id: Optional[int] = Field(
        None, description="ID of the user whose notes to fetch"
    )
    lead_id: Optional[str] = Field(
        None, description="ID of the lead whose notes to fetch"
    )
    deal_id: Optional[int] = Field(
        None, description="ID of the deal whose notes to fetch"
    )
    person_id: Optional[int] = Field(
        None, description="ID of the person whose notes to fetch"
    )
    org_id: Optional[int] = Field(
        None, description="ID of the organization whose notes to fetch"
    )
    project_id: Optional[int] = Field(
        None, description="ID of the project whose notes to fetch"
    )
    start: Optional[int] = Field(
        None, description="Pagination start offset"
    )
    limit: Optional[int] = Field(
        None, description="Items shown per page"
    )
    sort: Optional[str] = Field(
        None,
        description="Comma separated field names with sorting direction"
    )
    start_date: Optional[str] = Field(
        None, description="Fetch notes added from this date (YYYY-MM-DD)"
    )
    end_date: Optional[str] = Field(
        None, description="Fetch notes added until this date (YYYY-MM-DD)"
    )
    pinned_to_lead_flag: Optional[bool] = Field(
        None, description="Filter by note pinned to lead state"
    )
    pinned_to_deal_flag: Optional[bool] = Field(
        None, description="Filter by note pinned to deal state"
    )
    pinned_to_organization_flag: Optional[bool] = Field(
        None, description="Filter by note pinned to organization state"
    )
    pinned_to_person_flag: Optional[bool] = Field(
        None, description="Filter by note pinned to person state"
    )
    pinned_to_project_flag: Optional[bool] = Field(
        None, description="Filter by note pinned to project state"
    )


class AddNoteBody(BaseModel):
    """Body parameters for POST /v1/notes."""

    content: str = Field(
        ..., description="Content of the note in HTML format"
    )
    lead_id: Optional[str] = Field(
        None, description="ID of the lead to attach the note to"
    )
    deal_id: Optional[int] = Field(
        None, description="ID of the deal to attach the note to"
    )
    person_id: Optional[int] = Field(
        None, description="ID of the person this note will be attached to"
    )
    org_id: Optional[int] = Field(
        None, description="ID of the organization this note will be attached to"
    )
    project_id: Optional[int] = Field(
        None, description="ID of the project this note will be attached to"
    )
    user_id: Optional[int] = Field(
        None, description="User ID that will be marked as author"
    )
    add_time: Optional[str] = Field(
        None,
        description="Optional creation date & time of the note (YYYY-MM-DD HH:MM:SS)"
    )
    pinned_to_lead_flag: Optional[bool] = Field(
        None, description="Whether the note is pinned to the lead"
    )
    pinned_to_deal_flag: Optional[bool] = Field(
        None, description="Whether the note is pinned to the deal"
    )
    pinned_to_organization_flag: Optional[bool] = Field(
        None, description="Whether the note is pinned to the organization"
    )
    pinned_to_person_flag: Optional[bool] = Field(
        None, description="Whether the note is pinned to the person"
    )
    pinned_to_project_flag: Optional[bool] = Field(
        None, description="Whether the note is pinned to the project"
    )


class AddCommentBody(BaseModel):
    """Body parameters for POST /v1/notes/{id}/comments."""

    content: str = Field(
        ..., description="Content of the comment in HTML format"
    )


class UpdateNoteBody(BaseModel):
    """Body parameters for PUT /v1/notes/{id}."""

    content: Optional[str] = Field(
        None, description="Content of the note in HTML format"
    )
    lead_id: Optional[str] = Field(
        None, description="ID of the lead the note will be attached to"
    )
    deal_id: Optional[int] = Field(
        None, description="ID of the deal the note will be attached to"
    )
    person_id: Optional[int] = Field(
        None, description="ID of the person the note will be attached to"
    )
    org_id: Optional[int] = Field(
        None, description="ID of the organization the note will be attached to"
    )
    project_id: Optional[int] = Field(
        None, description="ID of the project the note will be attached to"
    )
    user_id: Optional[int] = Field(
        None, description="User ID that will be marked as author"
    )
    add_time: Optional[str] = Field(
        None,
        description="Optional creation date & time of the note (YYYY-MM-DD HH:MM:SS)"
    )
    pinned_to_lead_flag: Optional[bool] = Field(
        None, description="Whether the note is pinned to the lead"
    )
    pinned_to_deal_flag: Optional[bool] = Field(
        None, description="Whether the note is pinned to the deal"
    )
    pinned_to_organization_flag: Optional[bool] = Field(
        None, description="Whether the note is pinned to the organization"
    )
    pinned_to_person_flag: Optional[bool] = Field(
        None, description="Whether the note is pinned to the person"
    )
    pinned_to_project_flag: Optional[bool] = Field(
        None, description="Whether the note is pinned to the project"
    )


class UpdateCommentBody(BaseModel):
    """Body parameters for PUT /v1/notes/{id}/comments/{commentId}."""

    content: str = Field(
        ..., description="Content of the comment in HTML format"
    )


class GetNoteCommentsParams(BaseModel):
    """Query parameters for GET /v1/notes/{id}/comments."""

    start: Optional[int] = Field(
        None, description="Pagination start offset"
    )
    limit: Optional[int] = Field(
        None, description="Items shown per page"
    )
