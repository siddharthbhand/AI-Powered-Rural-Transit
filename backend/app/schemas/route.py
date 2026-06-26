from datetime import datetime

from pydantic import BaseModel


class RouteBase(BaseModel):
    route_name: str
    source: str
    destination: str
    distance_km: int
    estimated_time: str
    status: str = "Active"


class RouteCreate(RouteBase):
    pass


class RouteUpdate(RouteBase):
    pass


class RouteResponse(RouteBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True