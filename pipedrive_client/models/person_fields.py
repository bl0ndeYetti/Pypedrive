from typing import Optional, List
from pydantic import BaseModel, Field
from .common import FieldOption

class GetPersonFieldsParams(BaseModel):
    """Query parameters for GET /v1/personFields"""
    start: Optional[int] = Field(None, description="Pagination start")
    limit: Optional[int] = Field(None, description="Items shown per page")

class PersonFieldOption(FieldOption):
    """Option item used with enum or set field types."""

class AddPersonFieldBody(BaseModel):
    """Body parameters for POST /v1/personFields"""
    name: str = Field(..., description="The name of the field")
    field_type: str = Field(..., description="The type of the field")
    options: Optional[List[PersonFieldOption]] = Field(
        None,
        description="Options for set or enum field types as sequential objects",
    )
    add_visible_flag: Optional[bool] = Field(
        True,
        description="Whether the field is available in the add new modal",
    )

class UpdatePersonFieldBody(BaseModel):
    """Body parameters for PUT /v1/personFields/{id}"""
    name: Optional[str] = Field(None, description="The name of the field")
    options: Optional[List[PersonFieldOption]] = Field(
        None,
        description="Options for set or enum field types",
    )
    add_visible_flag: Optional[bool] = Field(
        None,
        description="Whether the field is available in the add new modal",
    )

class DeletePersonFieldsParams(BaseModel):
    """Query parameters for DELETE /v1/personFields"""
    ids: str = Field(..., description="Comma-separated IDs to delete")
