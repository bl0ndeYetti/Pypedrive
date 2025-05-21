from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field

class FilterTypeEnum(str, Enum):
    deals = "deals"
    leads = "leads"
    org = "org"
    people = "people"
    products = "products"
    activity = "activity"
    projects = "projects"

class GetFiltersParams(BaseModel):
    """Query parameters for GET /v1/filters"""

    type: Optional[FilterTypeEnum] = Field(
        None, description="The types of filters to fetch"
    )

class FilterCreateModel(BaseModel):
    """Body parameters for POST /v1/filters"""

    name: str = Field(..., description="The name of the filter")
    conditions: dict = Field(
        ..., description="The conditions of the filter as a JSON object"
    )
    type: FilterTypeEnum = Field(..., description="The type of filter to create")

class FilterUpdateModel(BaseModel):
    """Body parameters for PUT /v1/filters/{id}"""

    name: Optional[str] = Field(None, description="The name of the filter")
    conditions: Optional[dict] = Field(
        None, description="The conditions of the filter as a JSON object"
    )

class DeleteFiltersParams(BaseModel):
    """Query parameters for DELETE /v1/filters"""

    ids: str = Field(..., description="Comma-separated filter IDs to delete")
