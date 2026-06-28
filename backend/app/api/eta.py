from fastapi import APIRouter

from app.schemas.eta import (
    ETARequest,
    ETAResponse,
)
from app.services.eta_service import ETAService


router = APIRouter(
    prefix="/eta",
    tags=["ETA"],
)


@router.post(
    "/calculate",
    response_model=ETAResponse,
)
def calculate_eta(
    request: ETARequest,
):

    result = ETAService.calculate_eta(
        start_lat=request.start_lat,
        start_lon=request.start_lon,
        end_lat=request.end_lat,
        end_lon=request.end_lon,
        speed=request.speed,
    )

    return result