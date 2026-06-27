from typing import List

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.bus_location import (
    BusLocationCreate,
    BusLocationUpdate,
    BusLocationResponse,
)
from app.services.bus_location_service import BusLocationService

router = APIRouter(
    prefix="/bus-locations",
    tags=["Bus Locations"],
)


@router.post(
    "/",
    response_model=BusLocationResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_location(
    location: BusLocationCreate,
    db: Session = Depends(get_db),
):
    db_location = BusLocationService.create_location(db, location)

    if not db_location:
        raise HTTPException(
            status_code=404,
            detail="Bus not found",
        )

    return db_location


@router.get(
    "/",
    response_model=List[BusLocationResponse],
)
def get_all_locations(
    db: Session = Depends(get_db),
):
    return BusLocationService.get_all_locations(db)


@router.get(
    "/{location_id}",
    response_model=BusLocationResponse,
)
def get_location(
    location_id: int,
    db: Session = Depends(get_db),
):
    location = BusLocationService.get_location_by_id(
        db,
        location_id,
    )

    if not location:
        raise HTTPException(
            status_code=404,
            detail="Location not found",
        )

    return location


@router.get(
    "/bus/{bus_id}",
    response_model=List[BusLocationResponse],
)
def get_locations_by_bus(
    bus_id: int,
    db: Session = Depends(get_db),
):
    return BusLocationService.get_locations_by_bus(
        db,
        bus_id,
    )


@router.get(
    "/bus/{bus_id}/latest",
    response_model=BusLocationResponse,
)
def get_latest_location(
    bus_id: int,
    db: Session = Depends(get_db),
):
    location = BusLocationService.get_latest_location(
        db,
        bus_id,
    )

    if not location:
        raise HTTPException(
            status_code=404,
            detail="Location not found",
        )

    return location


@router.put(
    "/{location_id}",
    response_model=BusLocationResponse,
)
def update_location(
    location_id: int,
    location: BusLocationUpdate,
    db: Session = Depends(get_db),
):
    updated = BusLocationService.update_location(
        db,
        location_id,
        location,
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Location not found",
        )

    return updated


@router.delete(
    "/{location_id}",
)
def delete_location(
    location_id: int,
    db: Session = Depends(get_db),
):
    deleted = BusLocationService.delete_location(
        db,
        location_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Location not found",
        )

    return {
        "message": "Location deleted successfully"
    }