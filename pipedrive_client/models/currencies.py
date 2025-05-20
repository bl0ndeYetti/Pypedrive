from typing import Optional, List
from pydantic import BaseModel, Field


class GetCurrenciesParams(BaseModel):
    """Query parameters for GET /v1/currencies."""

    term: Optional[str] = Field(
        None,
        description="Optional search term for currency name or code"
    )


class Currency(BaseModel):
    """Currency information."""

    id: int = Field(..., description="ID of the currency")
    code: str = Field(..., description="Currency code")
    name: str = Field(..., description="Name of the currency")
    decimal_points: int = Field(..., description="Amount of decimal points")
    symbol: str = Field(..., description="Currency symbol")
    active_flag: bool = Field(..., description="Whether the currency is active")
    is_custom_flag: bool = Field(..., description="Whether the currency is custom")


class GetCurrenciesResponse(BaseModel):
    """Response model for GET /v1/currencies."""

    success: bool = Field(..., description="Whether the request was successful")
    data: List[Currency] = Field(..., description="The array of currencies")

