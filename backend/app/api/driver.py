from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.driver_location import DriverLocationUpdate
from app.services.driver_service import DriverService

router = APIRouter(
    prefix="/driver",
    tags=["Driver"],
)


@router.post("/location/{bus_id}")
async def update_driver_location(
    bus_id: int,
    location: DriverLocationUpdate,
    db: Session = Depends(get_db),
):

    await DriverService.update_driver_location(
        db=db,
        bus_id=bus_id,
        latitude=location.latitude,
        longitude=location.longitude,
        speed=location.speed,
        heading=location.heading,
    )

    return {
        "message": "Driver location updated successfully"
    }