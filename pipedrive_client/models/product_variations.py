from typing import Optional, List
from pydantic import BaseModel, Field
from .common import Price

class ProductVariationCreateModel(BaseModel):
    name: str
    # product_id is part of the URL path, not the body
    prices: Optional[List[Price]] = None # Note V2 price structure

class ProductVariationUpdateModel(BaseModel):
    name: Optional[str] = None
    prices: Optional[List[Price]] = None