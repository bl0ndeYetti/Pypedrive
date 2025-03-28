from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field
from .common import Price

class ProductCreateModel(BaseModel):
    name: str
    code: Optional[str] = None
    description: Optional[str] = None
    unit: Optional[str] = None
    tax: Optional[float] = 0.0
    category: Optional[str] = None
    is_linkable: Optional[bool] = Field(None, alias='selectable') # Alias for v1 name
    visible_to: Optional[int] = None # 1, 3, 5, 7
    owner_id: Optional[int] = None
    prices: Optional[List[Price]] = None # Note: Structure differs slightly from v1
    custom_fields: Optional[Dict[str, Any]] = None
    add_time: Optional[str] = None # YYYY-MM-DD HH:MM:SS or RFC3339

    class Config:
        validate_by_name = True
        extra = 'allow'

class ProductUpdateModel(BaseModel):
    name: Optional[str] = None
    code: Optional[str] = None
    description: Optional[str] = None
    unit: Optional[str] = None
    tax: Optional[float] = None
    category: Optional[str] = None
    is_linkable: Optional[bool] = Field(None, alias='selectable')
    visible_to: Optional[int] = None
    owner_id: Optional[int] = None
    prices: Optional[List[Price]] = Field(None, description="Note: Replaces the entire existing prices array")
    custom_fields: Optional[Dict[str, Any]] = None

    class Config:
        validate_by_name = True
        extra = 'allow'