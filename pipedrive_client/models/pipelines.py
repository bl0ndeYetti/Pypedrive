from typing import Optional
from pydantic import BaseModel, Field

class PipelineCreateModel(BaseModel):
    name: str
    is_deal_probability_enabled: Optional[bool] = Field(None, alias='deal_probability')
    # order_nr is read-only in V2 create/update

    class Config:
        validate_by_name = True

class PipelineUpdateModel(BaseModel):
    name: Optional[str] = None
    is_deal_probability_enabled: Optional[bool] = Field(None, alias='deal_probability')
    # order_nr is read-only

    class Config:
        validate_by_name = True