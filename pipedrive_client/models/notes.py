from typing import Optional
from pydantic import BaseModel, Field


class NoteUser(BaseModel):
    """User who created or modified the note."""

    email: Optional[str] = Field(None, description="User email")
    icon_url: Optional[str] = Field(None, description="URL of the avatar")
    is_you: Optional[bool] = Field(None, description="Whether it is the current user")
    name: Optional[str] = Field(None, description="Name of the user")


class NoteDealReference(BaseModel):
    """Minimal information about the related deal."""

    title: Optional[str] = Field(None, description="Deal title")


class NoteOrganizationReference(BaseModel):
    """Minimal information about the related organization."""

    name: Optional[str] = Field(None, description="Organization name")


class NotePersonReference(BaseModel):
    """Minimal information about the related person."""

    name: Optional[str] = Field(None, description="Person name")


class NoteProjectReference(BaseModel):
    """Minimal information about the related project."""

    title: Optional[str] = Field(None, description="Project title")


class Note(BaseModel):
    """Note response object."""

    id: int = Field(..., description="ID of the note")
    active_flag: Optional[bool] = Field(None, description="Whether the note is active")
    add_time: Optional[str] = Field(None, description="Note creation date")
    content: Optional[str] = Field(None, description="HTML content of the note")
    lead_id: Optional[str] = Field(None, description="ID of the linked lead")
    deal_id: Optional[int] = Field(None, description="ID of the linked deal")
    last_update_user_id: Optional[int] = Field(None, description="ID of last user who updated")
    org_id: Optional[int] = Field(None, description="ID of the linked organization")
    person_id: Optional[int] = Field(None, description="ID of the linked person")
    project_id: Optional[int] = Field(None, description="ID of the linked project")
    organization: Optional[NoteOrganizationReference] = Field(
        None, description="Organization attached to the note"
    )
    deal: Optional[NoteDealReference] = Field(
        None, description="Deal attached to the note"
    )
    person: Optional[NotePersonReference] = Field(
        None, description="Person attached to the note"
    )
    project: Optional[NoteProjectReference] = Field(
        None, description="Project attached to the note"
    )
    pinned_to_lead_flag: Optional[bool] = Field(
        None, description="Whether pinned to a lead"
    )
    pinned_to_deal_flag: Optional[bool] = Field(
        None, description="Whether pinned to a deal"
    )
    pinned_to_organization_flag: Optional[bool] = Field(
        None, description="Whether pinned to an organization"
    )
    pinned_to_person_flag: Optional[bool] = Field(
        None, description="Whether pinned to a person"
    )
    pinned_to_project_flag: Optional[bool] = Field(
        None, description="Whether pinned to a project"
    )
    update_time: Optional[str] = Field(
        None, description="Last update time"
    )
    user_id: Optional[int] = Field(None, description="Author ID")
    user: Optional[NoteUser] = Field(None, description="Author info")


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
