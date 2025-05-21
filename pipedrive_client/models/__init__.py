# Pipedrive API v2 Models
# Expose models if needed, or just use for internal type hinting

from .filters import FilterCreateModel, FilterUpdateModel, GetFiltersParams, DeleteFiltersParams
from .goals import (
    GoalCreateModel,
    GoalUpdateModel,
    FindGoalsParams,
    GoalResultParams,
    GoalTypeNameEnum,
    GoalAssigneeTypeEnum,
    GoalTrackingMetricEnum,
    GoalIntervalEnum,
)
from .leads import (
    LeadCreateModel,
    LeadUpdateModel,
    GetLeadsParams,
    SearchLeadsParams,
    ConvertLeadToDealBody,
)
from .notes import (
    NoteCreateModel,
    NoteUpdateModel,
    GetNotesParams,
    CommentCreateModel,
    CommentUpdateModel,
)
from .webhooks import WebhookCreateModel, EventActionEnum, EventObjectEnum

__all__ = [
    "FilterCreateModel",
    "FilterUpdateModel",
    "GetFiltersParams",
    "DeleteFiltersParams",
    "GoalCreateModel",
    "GoalUpdateModel",
    "FindGoalsParams",
    "GoalResultParams",
    "GoalTypeNameEnum",
    "GoalAssigneeTypeEnum",
    "GoalTrackingMetricEnum",
    "GoalIntervalEnum",
    "LeadCreateModel",
    "LeadUpdateModel",
    "GetLeadsParams",
    "SearchLeadsParams",
    "ConvertLeadToDealBody",
    "NoteCreateModel",
    "NoteUpdateModel",
    "GetNotesParams",
    "CommentCreateModel",
    "CommentUpdateModel",
    "WebhookCreateModel",
    "EventActionEnum",
    "EventObjectEnum",
]
