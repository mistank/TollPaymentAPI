from pydantic import BaseModel


class LocationBase(BaseModel):
    city: str
    class Config:
        orm_mode = True
        arbitrary_types_allowed = True
        from_orm = True
        from_attributes = True