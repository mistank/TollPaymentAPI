from decimal import Decimal

from pydantic import BaseModel


class PriceBase(BaseModel):
    price_id:int
    price: Decimal
    entry_location_id: int
    exit_location_id: int

    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
