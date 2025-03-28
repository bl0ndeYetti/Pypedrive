from typing import Optional, List, Dict, Any, Union
from pydantic import BaseModel, Field
from .common import Address, Attendee, Participant, BaseCustomFieldsModel

class ActivityCreateModel(BaseCustomFieldsModel):
    subject: str
    type: Optional[str] = None
    public_description: Optional[str] = None
    note: Optional[str] = None
    due_date: Optional[str] = None # YYYY-MM-DD
    due_time: Optional[str] = None # HH:MM
    duration: Optional[str] = None # HH:MM
    owner_id: Optional[int] = None # Renamed from user_id
    deal_id: Optional[int] = None
    person_id: Optional[int] = Field(None, description="Read-only in v2, set via participants")
    participants: Optional[List[Participant]] = None
    org_id: Optional[int] = None
    location: Optional[Union[str, Address]] = None # Can be simple string or structured Address
    busy: Optional[bool] = Field(None, alias='busy_flag') # Alias for v1 compatibility if needed, prefer 'busy'
    attendees: Optional[List[Attendee]] = None
    done: Optional[bool] = None
    # Add other relevant V2 fields based on documentation

    class Config:
        validate_by_name = True
        # Pydantic v2: use_enum_values = True

class ActivityUpdateModel(BaseCustomFieldsModel):
    subject: Optional[str] = None
    type: Optional[str] = None
    public_description: Optional[str] = None
    note: Optional[str] = None
    due_date: Optional[str] = None # YYYY-MM-DD
    due_time: Optional[str] = None # HH:MM
    duration: Optional[str] = None # HH:MM
    owner_id: Optional[int] = None # Renamed from user_id
    deal_id: Optional[int] = None
    person_id: Optional[int] = Field(None, description="Read-only in v2, set via participants")
    participants: Optional[List[Participant]] = None
    org_id: Optional[int] = None
    location: Optional[Union[str, Address]] = None # Can be simple string or structured Address
    busy: Optional[bool] = Field(None, alias='busy_flag')
    attendees: Optional[List[Attendee]] = None
    done: Optional[bool] = None
    # Add other relevant V2 fields based on documentation

    class Config:
        validate_by_name = True
        # Pydantic v2: use_enum_values = True