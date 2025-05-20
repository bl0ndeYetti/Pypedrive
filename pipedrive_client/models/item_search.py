from typing import Optional
from pydantic import BaseModel, Field

class SearchItemsParams(BaseModel):
    """Query parameters for GET /api/v2/itemSearch"""

    term: str = Field(..., description="Search term. Minimum 2 characters (1 if exact_match). URL encoded")
    item_types: Optional[str] = Field(
        None,
        description="Comma-separated list of item types to search (deal, person, organization, product, lead, file, mail_attachment, project)",
    )
    fields: Optional[str] = Field(
        None,
        description="Comma-separated list of fields to search in for each item type",
    )
    search_for_related_items: Optional[bool] = Field(
        None,
        description="Include related leads and deals for persons and organizations",
    )
    exact_match: Optional[bool] = Field(
        None,
        description="Return only full exact matches. Case insensitive",
    )
    include_fields: Optional[str] = Field(
        None,
        description="Optional additional fields to include in results (e.g. deal.cc_email, person.picture, product.price)",
    )
    limit: Optional[int] = Field(
        None,
        description="Number of items to return (max 500, default 100)",
    )
    cursor: Optional[str] = Field(
        None,
        description="Opaque marker for pagination representing first item on next page",
    )


class SearchItemsByFieldParams(BaseModel):
    """Query parameters for GET /api/v2/itemSearch/field"""

    term: str = Field(
        ...,
        description="Search term. Minimum 2 characters (1 if match is 'exact'). URL encoded",
    )
    entity_type: str = Field(
        ...,
        description="Item type of the field (deal, lead, person, organization, product, project)",
    )
    match: Optional[str] = Field(
        None,
        description="Type of match: 'exact', 'beginning', or 'middle'. Case sensitive",
    )
    field: str = Field(
        ...,
        description="Key of the field to search",
    )
    limit: Optional[int] = Field(
        None,
        description="Number of entries to return (max 500, default 100)",
    )
    cursor: Optional[str] = Field(
        None,
        description="Opaque marker for pagination representing first item on next page",
    )

    class Config:
        validate_by_name = True
