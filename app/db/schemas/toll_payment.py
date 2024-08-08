import re

from pydantic import BaseModel, field_validator

from app.db.schemas.location import LocationBase


class TollPaymentBase(BaseModel):
    entry_location: LocationBase
    exit_location: LocationBase
    card_number: str
    ccv: str
    first_name: str
    last_name: str

    @field_validator('card_number')
    def validate_card_number(cls, value):
        if not re.match(r'^\d{16}$', value):
            raise ValueError('Card number must be 16 digits')
        return value

    @field_validator('ccv')
    def validate_ccv(cls, value):
        if not re.match(r'^\d{3,4}$', value):
            raise ValueError('CCV must be 3 or 4 digits')
        return value

class TollPayment(TollPaymentBase):
    toll_price: float
    class Config:
        orm_mode = True
