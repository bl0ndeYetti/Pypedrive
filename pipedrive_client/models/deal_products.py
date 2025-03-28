from typing import Optional
from pydantic import BaseModel, Field

class DealProductAttachModel(BaseModel):
    product_id: int
    item_price: float
    quantity: float
    discount: Optional[float] = 0.0
    discount_type: Optional[str] = Field('percentage', description="'percentage' or 'amount'")
    # duration: Optional[float] = 1.0 # Duration seems removed/implicit in v2 examples? Verify.
    # duration_unit: Optional[str] = None # Verify if used in v2
    tax: Optional[float] = 0.0
    tax_method: Optional[str] = Field('exclusive', description="'inclusive', 'exclusive', 'none'")
    is_enabled: Optional[bool] = Field(True, alias='enabled_flag') # V1 name compatibility
    comments: Optional[str] = None
    product_variation_id: Optional[int] = None

    class Config:
        validate_by_name = True

class DealProductUpdateModel(BaseModel):
    product_id: Optional[int] = None # Typically not changed, but maybe allowed?
    item_price: Optional[float] = None
    quantity: Optional[float] = None
    discount: Optional[float] = None
    discount_type: Optional[str] = None
    # duration: Optional[float] = None
    # duration_unit: Optional[str] = None
    tax: Optional[float] = None
    tax_method: Optional[str] = None
    is_enabled: Optional[bool] = Field(None, alias='enabled_flag')
    comments: Optional[str] = None
    product_variation_id: Optional[int] = None

    class Config:
        validate_by_name = True