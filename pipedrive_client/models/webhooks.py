from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field

class EventActionEnum(str, Enum):
    create = "create"
    change = "change"
    delete = "delete"
    all = "*"

class EventObjectEnum(str, Enum):
    activity = "activity"
    deal = "deal"
    lead = "lead"
    note = "note"
    organization = "organization"
    person = "person"
    pipeline = "pipeline"
    product = "product"
    stage = "stage"
    user = "user"
    all = "*"

class WebhookCreateModel(BaseModel):
    """Body parameters for POST /v1/webhooks"""

    subscription_url: str = Field(
        ..., description="Public URL where notifications will be sent"
    )
    event_action: EventActionEnum = Field(
        ..., description="Type of action to receive notifications about"
    )
    event_object: EventObjectEnum = Field(
        ..., description="Type of object to receive notifications about"
    )
    user_id: Optional[int] = Field(
        None,
        description="User ID that authorizes the webhook (defaults to current user)",
    )
    http_auth_user: Optional[str] = Field(
        None, description="HTTP auth username for the subscription URL"
    )
    http_auth_password: Optional[str] = Field(
        None, description="HTTP auth password for the subscription URL"
    )
    version: Optional[str] = Field(
        "2.0", description="Webhook version"
    )
