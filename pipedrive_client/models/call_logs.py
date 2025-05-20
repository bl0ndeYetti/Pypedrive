from typing import Optional, List
from pydantic import BaseModel, Field


class AddCallLogBody(BaseModel):
    """Body parameters for POST /v1/callLogs."""

    to_phone_number: str = Field(..., description="The number called")
    outcome: str = Field(..., description="Describes the outcome of the call")
    start_time: str = Field(..., description="Call start time in UTC (YYYY-MM-DD HH:MM:SS)")
    end_time: str = Field(..., description="Call end time in UTC (YYYY-MM-DD HH:MM:SS)")
    user_id: Optional[int] = Field(
        None,
        description="Owner ID of the call log"
    )
    activity_id: Optional[int] = Field(
        None,
        description="Activity ID to convert into a call log"
    )
    subject: Optional[str] = Field(None, description="Name of the activity this call is attached to")
    duration: Optional[str] = Field(None, description="Duration of the call in seconds")
    from_phone_number: Optional[str] = Field(None, description="The number that made the call")
    person_id: Optional[int] = Field(None, description="ID of the person associated with the call")
    org_id: Optional[int] = Field(None, description="ID of the organization associated with the call")
    deal_id: Optional[int] = Field(
        None,
        description="ID of the deal associated with the call (exclusive with lead_id)"
    )
    lead_id: Optional[str] = Field(
        None,
        description="Lead ID (UUID) associated with the call (exclusive with deal_id)"
    )
    note: Optional[str] = Field(None, description="HTML formatted note for the call log")


class CallLog(AddCallLogBody):
    """Call log response object."""

    id: str = Field(..., description="Call log identifier")
    has_recording: Optional[bool] = Field(None, description="Whether an audio recording is attached")
    company_id: Optional[int] = Field(None, description="Company ID of the owner of the call log")


class GetUserCallLogsParams(BaseModel):
    """Query parameters for GET /v1/callLogs."""

    start: Optional[int] = Field(0, description="Pagination start")
    limit: Optional[int] = Field(
        None, description="Number of entries to return (max 50)"
    )


class AddCallLogAudioFileBody(BaseModel):
    """Body parameters for POST /v1/callLogs/{id}/recordings."""

    file: bytes = Field(..., description="Audio file supported by HTML5")

