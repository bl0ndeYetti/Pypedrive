from enum import Enum
from typing import Optional, List, Dict, Any
from pydantic import BaseModel, Field

class GoalTypeNameEnum(str, Enum):
    deals_won = "deals_won"
    deals_progressed = "deals_progressed"
    activities_completed = "activities_completed"
    activities_added = "activities_added"
    deals_started = "deals_started"
    revenue_forecast = "revenue_forecast"

class GoalAssigneeTypeEnum(str, Enum):
    person = "person"
    company = "company"
    team = "team"

class GoalTrackingMetricEnum(str, Enum):
    quantity = "quantity"
    sum = "sum"

class GoalIntervalEnum(str, Enum):
    weekly = "weekly"
    monthly = "monthly"
    quarterly = "quarterly"
    yearly = "yearly"

class GoalAssignee(BaseModel):
    id: int = Field(..., description="ID of the assignee")
    type: GoalAssigneeTypeEnum = Field(..., description="Type of the assignee")

class GoalType(BaseModel):
    name: GoalTypeNameEnum = Field(..., description="Type of the goal")
    params: Optional[Dict[str, Any]] = Field(
        None,
        description="Additional parameters like pipeline_id, stage_id or activity_type_id",
    )

class ExpectedOutcome(BaseModel):
    target: float = Field(..., description="Numeric value of the outcome")
    tracking_metric: GoalTrackingMetricEnum = Field(
        ..., description="Tracking metric of the outcome"
    )
    currency_id: Optional[int] = Field(
        None,
        description="Currency ID, used when tracking_metric is 'sum'",
    )

class GoalDuration(BaseModel):
    start: str = Field(..., description="Start date YYYY-MM-DD")
    end: Optional[str] = Field(None, description="End date YYYY-MM-DD or null")

class FindGoalsParams(BaseModel):
    """Query parameters for GET /v1/goals/find"""

    type_name: Optional[GoalTypeNameEnum] = Field(None, alias="type.name")
    title: Optional[str] = None
    is_active: Optional[bool] = None
    assignee_id: Optional[int] = Field(None, alias="assignee.id")
    assignee_type: Optional[GoalAssigneeTypeEnum] = Field(
        None, alias="assignee.type"
    )
    expected_outcome_target: Optional[float] = Field(
        None, alias="expected_outcome.target"
    )
    expected_outcome_tracking_metric: Optional[GoalTrackingMetricEnum] = Field(
        None, alias="expected_outcome.tracking_metric"
    )
    expected_outcome_currency_id: Optional[int] = Field(
        None, alias="expected_outcome.currency_id"
    )
    type_params_pipeline_id: Optional[List[int]] = Field(
        None, alias="type.params.pipeline_id"
    )
    type_params_stage_id: Optional[int] = Field(
        None, alias="type.params.stage_id"
    )
    type_params_activity_type_id: Optional[List[int]] = Field(
        None, alias="type.params.activity_type_id"
    )
    period_start: Optional[str] = Field(None, alias="period.start")
    period_end: Optional[str] = Field(None, alias="period.end")

class GoalCreateModel(BaseModel):
    """Body parameters for POST /v1/goals"""

    title: str = Field(..., description="Title of the goal")
    assignee: GoalAssignee = Field(..., description="Goal assignee")
    type: GoalType = Field(..., description="Goal type definition")
    expected_outcome: ExpectedOutcome = Field(
        ..., description="Expected outcome of the goal"
    )
    duration: GoalDuration = Field(..., description="Goal duration")
    interval: GoalIntervalEnum = Field(..., description="Goal interval")

class GoalUpdateModel(BaseModel):
    """Body parameters for PUT /v1/goals/{id}"""

    title: Optional[str] = None
    assignee: Optional[GoalAssignee] = None
    type: Optional[GoalType] = None
    expected_outcome: Optional[ExpectedOutcome] = None
    duration: Optional[GoalDuration] = None
    interval: Optional[GoalIntervalEnum] = None

class GoalResultParams(BaseModel):
    """Query parameters for GET /v1/goals/{id}/results"""

    period_start: str = Field(..., alias="period.start")
    period_end: str = Field(..., alias="period.end")
