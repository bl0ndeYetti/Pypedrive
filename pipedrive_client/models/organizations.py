from typing import Optional, List, Dict, Any, Union # Added Union
from pydantic import BaseModel, Field
from .common import Address # Removed BaseCustomFieldsModel

class OrganizationCreateModel(BaseModel):
    name: str
    owner_id: Optional[int] = None
    visible_to: Optional[int] = None # 1, 3, 5, 7
    label_ids: Optional[List[int]] = None
    address: Optional[Union[str, Address]] = None # Can be simple string or structured Address object
    custom_fields: Optional[Dict[str, Any]] = None
    add_time: Optional[str] = None # YYYY-MM-DD HH:MM:SS or RFC3339

    class Config:
        extra = 'allow'

class OrganizationUpdateModel(BaseModel):
    name: Optional[str] = None
    owner_id: Optional[int] = None
    visible_to: Optional[int] = None # 1, 3, 5, 7
    label_ids: Optional[List[int]] = None
    address: Optional[Union[str, Address]] = None
    custom_fields: Optional[Dict[str, Any]] = None

    class Config:
        extra = 'allow'