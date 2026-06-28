from pydantic import BaseModel


class ETARequest(BaseModel):

    start_lat: float
    start_lon: float

    end_lat: float
    end_lon: float

    speed: float


class ETAResponse(BaseModel):

    distance_km: float
    speed_kmh: float
    eta_minutes: int