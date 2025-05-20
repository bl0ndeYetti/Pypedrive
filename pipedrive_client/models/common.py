from typing import Optional, List, Dict, Any, Union
from pydantic import BaseModel, Field, validator

class BaseCustomFieldsModel(BaseModel):
    """Base model for objects that can have custom fields."""
    custom_fields: Optional[Dict[str, Any]] = Field(default_factory=dict)

class Address(BaseModel):
    """V2 Address structure (used for custom fields and standard org/person address)."""
    value: Optional[str] = None             # Full address string (e.g., for custom fields)
    route: Optional[str] = None
    street_number: Optional[str] = None
    sublocality: Optional[str] = None
    locality: Optional[str] = None
    admin_area_level_1: Optional[str] = None
    admin_area_level_2: Optional[str] = None
    country: Optional[str] = None
    postal_code: Optional[str] = None
    formatted_address: Optional[str] = None

class CurrencyValue(BaseModel):
    """V2 Currency structure (used for custom fields)."""
    value: Optional[float] = None
    currency: Optional[str] = None

class DateRange(BaseModel):
    """V2 Date Range structure (used for custom fields)."""
    value: Optional[str] = None # YYYY-MM-DD
    until: Optional[str] = None # YYYY-MM-DD

class TimeRange(BaseModel):
    """V2 Time Range structure (used for custom fields)."""
    value: Optional[str] = None # HH:MM:SS
    until: Optional[str] = None # HH:MM:SS

class MonetaryValue(BaseModel):
    value: float
    currency: str

class Price(BaseModel):
    product_id: Optional[int] = None # Present in Product object, not in Variation
    product_variation_id: Optional[int] = None # Present in Variation object
    price: float
    currency: str
    cost: Optional[float] = Field(None, alias='cost') # V1 name in Product Variation
    direct_cost: Optional[float] = Field(None, alias='direct_cost') # V2 name in Product

    class Config:
        validate_by_name = True

class PhoneEmailIMValue(BaseModel):
    value: str
    label: Optional[str] = 'work'
    primary: Optional[bool] = None

class Participant(BaseModel):
    person_id: int
    primary_flag: bool = Field(alias='primary') # V2 uses 'primary', V1 used 'primary_flag'

    class Config:
        validate_by_name = True
        
class Attendee(BaseModel):
    email_address: str
    name: Optional[str] = None
    status: Optional[str] = None # e.g., 'accepted', 'declined', 'noreply'
    is_organizer: Optional[int] = None # 0 or 1, V1 format still used? Check if boolean works.
    person_id: Optional[int] = None
    user_id: Optional[int] = None

class FieldOption(BaseModel):
    """Option item used with enum or set custom fields."""
    id: Optional[int] = Field(None, description="Existing option ID")
    label: str = Field(..., description="Displayed option label")
