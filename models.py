from pydantic import BaseModel
from typing import List

class ProductRequest(BaseModel):
    product_name: str

class PriceItem(BaseModel):
    site: str
    price: float

class ProductResponse(BaseModel):
    product: str
    prices: List[PriceItem]
    lowest_price: float
    alert: bool
    message: str
