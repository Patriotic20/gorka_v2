from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class ProductBase(BaseModel):
    barcode: str
    name: str
    quantity: Optional[int] = 0


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):
    barcode: Optional[str] = None
    name: Optional[str] = None
    quantity: Optional[int] = None


class ProductResponse(ProductBase):
    id: int
    create_at: datetime

    class Config:
        from_attributes = True
