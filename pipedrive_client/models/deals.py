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