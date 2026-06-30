from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.services.passenger_service import PassengerService

router = APIRouter(
    prefix="/passenger",
    tags=["Passenger"],
)


@router.get("/live-buses")
def get_live_buses(
    db: Session = Depends(get_db),
):

    return PassengerService.get_live_buses(db)


@router.get("/search")
def search_live_buses(
    source: str = Query(...),
    destination: str = Query(...),
    db: Session = Depends(get_db),
):

    return PassengerService.search_buses(
        db=db,
        source=source,
        destination=destination,
    )


@router.get("/bus/{bus_id}")
def get_bus_details(
    bus_id: int,
    db: Session = Depends(get_db),
):

    bus = PassengerService.get_bus_details(
        db=db,
        bus_id=bus_id,
    )

    if not bus:
        raise HTTPException(
            status_code=404,
            detail="Bus not found",
        )

    return bus