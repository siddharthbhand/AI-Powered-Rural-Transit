from pydantic import BaseModel
from datetime import datetime


class BusBase(BaseModel):
    bus_number: str
    bus_name: str
    operator_name: str
    source: str
    destination: str
    total_seats: int
    available_seats: int
    bus_type: str
    status: str = "Active"


class BusCreate(BusBase):
    pass


class BusUpdate(BusBase):
    pass


class BusResponse(BusBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True