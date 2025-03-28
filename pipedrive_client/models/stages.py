from typing import Optional
from pydantic import BaseModel, Field

class StageCreateModel(BaseModel):
    name: str
    pipeline_id: int
    order_nr: Optional[int] = None
    deal_probability: Optional[int] = None # Percentage 0-100
    is_deal_rot_enabled: Optional[bool] = Field(None, alias='rotten_flag')
    days_to_rotten: Optional[int] = Field(None, alias='rotten_days')

    class Config:
        validate_by_name = True

class StageUpdateModel(BaseModel):
    name: Optional[str] = None
    pipeline_id: Optional[int] = None # Usually not changed, but API might allow
    order_nr: Optional[int] = None
    deal_probability: Optional[int] = None
    is_deal_rot_enabled: Optional[bool] = Field(None, alias='rotten_flag')
    days_to_rotten: Optional[int] = Field(None, alias='rotten_days')

    class Config:
        validate_by_name = True