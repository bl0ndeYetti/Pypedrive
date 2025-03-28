from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field, validator
from .common import Address, PhoneEmailIMValue # Removed BaseCustomFieldsModel

class PersonCreateModel(BaseModel):
    name: Optional[str] = None # Required if first/last name not given
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    owner_id: Optional[int] = None
    org_id: Optional[int] = None
    emails: Optional[List[PhoneEmailIMValue]] = Field(None, alias='email') # Use alias for potential v1 name use
    phones: Optional[List[PhoneEmailIMValue]] = Field(None, alias='phone') # Use alias for potential v1 name use
    ims: Optional[List[PhoneEmailIMValue]] = Field(None, alias='im')       # Use alias for potential v1 name use
    visible_to: Optional[int] = None # 1, 3, 5, 7
    marketing_status: Optional[str] = None # e.g., 'subscribed', 'unsubscribed', etc. Requires marketing app access.
    label_ids: Optional[List[int]] = None
    custom_fields: Optional[Dict[str, Any]] = None
    add_time: Optional[str] = None # YYYY-MM-DD HH:MM:SS or RFC3339
    # Fields only included if contact sync enabled (birthday, job_title, postal_address, notes)
    birthday: Optional[str] = None # YYYY-MM-DD
    job_title: Optional[str] = None
    postal_address: Optional[Address] = None # Note: V2 uses nested object
    notes: Optional[str] = None

    @validator('name', always=True)
    def check_name_or_first_last(cls, v, values):
        if not v and not (values.get('first_name') is not None and values.get('last_name') is not None):
            raise ValueError('Either "name" or both "first_name" and "last_name" must be provided')
        # Ensure first/last name are not both empty strings if name isn't provided
        if not v and values.get('first_name') == "" and values.get('last_name') == "":
             raise ValueError('Both "first_name" and "last_name" cannot be empty if "name" is not provided')
        return v

    class Config:
        extra = 'allow'
        validate_by_name = True


class PersonUpdateModel(BaseModel):
    name: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    owner_id: Optional[int] = None
    org_id: Optional[int] = None
    emails: Optional[List[PhoneEmailIMValue]] = Field(None, alias='email')
    phones: Optional[List[PhoneEmailIMValue]] = Field(None, alias='phone')
    ims: Optional[List[PhoneEmailIMValue]] = Field(None, alias='im')
    visible_to: Optional[int] = None
    marketing_status: Optional[str] = None
    label_ids: Optional[List[int]] = None
    custom_fields: Optional[Dict[str, Any]] = None
    # Fields only included if contact sync enabled
    birthday: Optional[str] = None
    job_title: Optional[str] = None
    postal_address: Optional[Address] = None
    notes: Optional[str] = None

    @validator('name', always=True)
    def check_name_update(cls, v, values):
        # Allow partial updates, don't enforce name vs first/last unless all are present
        if v is None and values.get('first_name') is None and values.get('last_name') is None:
            return v # No name fields being updated
        if v is None and (values.get('first_name') == "" and values.get('last_name') == ""):
             raise ValueError('Both "first_name" and "last_name" cannot be empty if "name" is not provided')
        return v


    class Config:
        extra = 'allow'
        validate_by_name = True