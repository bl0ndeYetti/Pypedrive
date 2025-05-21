from typing import Optional, List
from enum import Enum
from pydantic import BaseModel, Field


class NoteFieldTypeEnum(str, Enum):
    """Possible field types for note fields."""

    address = "address"
    date = "date"
    daterange = "daterange"
    double = "double"
    enum = "enum"
    monetary = "monetary"
    org = "org"
    people = "people"
    phone = "phone"
    set = "set"
    text = "text"
    time = "time"
    timerange = "timerange"
    user = "user"
    varchar = "varchar"
    varchar_auto = "varchar_auto"
    visible_to = "visible_to"


class GetNoteFieldsParams(BaseModel):
    """Query parameters for GET /v1/noteFields."""

    pass


class NoteFieldOption(BaseModel):
    """Single option for an enum/set note field."""

    id: int = Field(..., description="Option identifier")
    label: str = Field(..., description="Human readable option label")


class NoteField(BaseModel):
    """Information about a note field."""

    id: int = Field(..., description="ID of the field")
    key: str = Field(..., description="Unique key of the field")
    name: str = Field(..., description="Field display name")
    field_type: NoteFieldTypeEnum = Field(
        ..., description="Type of the field"
    )
    active_flag: Optional[bool] = Field(
        None, description="Whether the field is active"
    )
    edit_flag: Optional[bool] = Field(
        None, description="Whether the field can be edited"
    )
    bulk_edit_allowed: Optional[bool] = Field(
        None, description="Whether the field supports bulk editing"
    )
    mandatory_flag: Optional[bool] = Field(
        None, description="Whether the field is mandatory"
    )
    options: Optional[List[NoteFieldOption]] = Field(
        None, description="List of selectable options for the field"
    )

