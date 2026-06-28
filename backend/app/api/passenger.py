from fastapi import APIRouter, Depends, Query
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
    print("===== LIVE BUSES API CALLED =====")

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