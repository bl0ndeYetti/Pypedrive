from typing import Optional
from pydantic import BaseModel, Field


class ActivityTypeCreateModel(BaseModel):
    """Body parameters for POST /v1/activityTypes."""

    name: str = Field(..., description="The name of the activity type")
    icon_key: str = Field(..., description="Icon graphic representing the type")
    color: Optional[str] = Field(
        None,
        description="Designated color in HEX format, e.g. 'FFFFFF'",
    )


class ActivityTypeUpdateModel(BaseModel):
    """Body parameters for PUT /v1/activityTypes/{id}."""

    name: Optional[str] = Field(None, description="The name of the activity type")
    icon_key: Optional[str] = Field(
        None, description="Icon graphic representing the type"
    )
    color: Optional[str] = Field(
        None, description="Designated color in HEX format"
    )
    order_nr: Optional[int] = Field(
        None,
        description="Order number used to sort activity types in selections",
    )


class DeleteActivityTypesParams(BaseModel):
    """Query parameters for DELETE /v1/activityTypes."""

    ids: str = Field(..., description="Comma-separated activity type IDs")
