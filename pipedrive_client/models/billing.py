from typing import Optional, List
from pydantic import BaseModel, Field


class AddOn(BaseModel):
    """Add-on information."""

    code: Optional[str] = Field(None, description="Identifier of the add-on")


class GetCompanyAddonsResponse(BaseModel):
    """Response model for GET /v1/billing/subscriptions/addons."""

    success: bool = Field(..., description="Whether the request was successful")
    data: Optional[List[AddOn]] = Field(
        None, description="List of add-ons enabled for the company"
    )

