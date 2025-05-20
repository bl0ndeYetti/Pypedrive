from typing import Optional, List
from pydantic import BaseModel, Field

class GetDealFieldsParams(BaseModel):
    """Query parameters for GET /v1/dealFields"""

    start: Optional[int] = Field(
        None, description="Pagination start offset"
    )
    limit: Optional[int] = Field(
        None, description="Items shown per page"
    )

class DealFieldOption(BaseModel):
    """Option item used with enum or set field types."""

    id: Optional[int] = Field(None, description="Existing option ID")
    label: str = Field(..., description="Displayed option label")

class AddDealFieldBody(BaseModel):
    """Body parameters for POST /v1/dealFields"""

    name: str = Field(..., description="The name of the field")
    field_type: str = Field(..., description="The type of the field")
    options: Optional[List[DealFieldOption]] = Field(
        None,
        description="Options for set or enum field types as sequential objects",
    )
    add_visible_flag: Optional[bool] = Field(
        True,
        description="Whether the field is available in the add new modal",
    )

class UpdateDealFieldBody(BaseModel):
    """Body parameters for PUT /v1/dealFields/{id}"""

    name: Optional[str] = Field(None, description="The name of the field")
    options: Optional[List[DealFieldOption]] = Field(
        None,
        description="Options for set or enum field types",
    )
    add_visible_flag: Optional[bool] = Field(
        None,
        description="Whether the field is available in the add new modal",
    )

class DeleteDealFieldsParams(BaseModel):
    """Query parameters for DELETE /v1/dealFields"""

    ids: str = Field(..., description="Comma-separated IDs to delete")
