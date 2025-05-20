from typing import Optional
from pydantic import BaseModel, Field

class StageCreateModel(BaseModel):
    """Body parameters for POST /api/v2/stages."""

    name: str = Field(..., description="Name of the stage")
    pipeline_id: int = Field(..., description="ID of the pipeline the stage belongs to")
    order_nr: Optional[int] = Field(
        None, description="Order number within the pipeline"
    )
    deal_probability: Optional[int] = Field(
        None, description="Success probability percentage of deals in this stage"
    )
    is_deal_rot_enabled: Optional[bool] = Field(
        None,
        alias="rotten_flag",
        description="Whether deals can become rotten in this stage",
    )
    days_to_rotten: Optional[int] = Field(
        None,
        alias="rotten_days",
        description="Number of days after which inactive deals become rotten",
    )

    class Config:
        validate_by_name = True

class StageUpdateModel(BaseModel):
    """Body parameters for PATCH /api/v2/stages/{id}."""

    name: Optional[str] = Field(None, description="Name of the stage")
    pipeline_id: Optional[int] = Field(
        None,
        description="ID of the pipeline the stage belongs to (usually unchanged)",
    )
    order_nr: Optional[int] = Field(
        None, description="Order number within the pipeline"
    )
    deal_probability: Optional[int] = Field(
        None, description="Success probability percentage of deals in this stage"
    )
    is_deal_rot_enabled: Optional[bool] = Field(
        None,
        alias="rotten_flag",
        description="Whether deals can become rotten in this stage",
    )
    days_to_rotten: Optional[int] = Field(
        None,
        alias="rotten_days",
        description="Number of days after which inactive deals become rotten",
    )

    class Config:
        validate_by_name = True


class GetStagesParams(BaseModel):
    """Query parameters for GET /api/v2/stages."""

    pipeline_id: Optional[int] = Field(
        None,
        description="ID of the pipeline to fetch stages for; fetches all if omitted",
    )
    sort_by: Optional[str] = Field(
        None,
        description="Field to sort by: id, update_time, add_time or order_nr",
    )
    sort_direction: Optional[str] = Field(
        None, description="Sorting direction: asc or desc"
    )
    limit: Optional[int] = Field(
        None,
        description="Limit of entries to return (max 500, default 100)",
    )
    cursor: Optional[str] = Field(
        None,
        description="Cursor representing the first item on the next page",
    )
