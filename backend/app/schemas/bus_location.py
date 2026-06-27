from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field, ConfigDict


class BusLocationBase(BaseModel):
    latitude: float = Field(
        ...,
        ge=-90,
        le=90,
        description="GPS Latitude"
    )

    longitude: float = Field(
        ...,
        ge=-180,
        le=180,
        description="GPS Longitude"
    )

    speed: Optional[float] = Field(
        default=None,
        ge=0,
        description="Current speed in km/h"
    )

    heading: Optional[float] = Field(
        default=None,
        ge=0,
        le=360,
        description="Direction in degrees"
    )


class BusLocationCreate(BusLocationBase):
    bus_id: int


class BusLocationUpdate(BaseModel):
    latitude: Optional[float] = Field(default=None, ge=-90, le=90)

    longitude: Optional[float] = Field(default=None, ge=-180, le=180)

    speed: Optional[float] = Field(default=None, ge=0)

    heading: Optional[float] = Field(default=None, ge=0, le=360)


class BusLocationResponse(BusLocationBase):
    id: int
    bus_id: int
    recorded_at: datetime
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)