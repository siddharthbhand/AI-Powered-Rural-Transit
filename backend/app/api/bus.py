from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.bus import (
    BusCreate,
    BusUpdate,
    BusResponse,
)

from app.services.bus_service import (
    get_all_buses,
    get_bus_by_id,
    get_bus_by_number,
    create_bus,
    update_bus,
    delete_bus,
)

router = APIRouter(
    prefix="/buses",
    tags=["Bus Management"],
)


@router.get("/", response_model=list[BusResponse])
def get_buses(db: Session = Depends(get_db)):
    return get_all_buses(db)


@router.get("/{bus_id}", response_model=BusResponse)
def get_bus(bus_id: int, db: Session = Depends(get_db)):
    bus = get_bus_by_id(db, bus_id)

    if not bus:
        raise HTTPException(
            status_code=404,
            detail="Bus not found"
        )

    return bus


@router.post("/", response_model=BusResponse)
def add_bus(bus: BusCreate, db: Session = Depends(get_db)):
    existing = get_bus_by_number(db, bus.bus_number)

    if existing:
        raise HTTPException(
            status_code=400,
            detail="Bus number already exists"
        )

    return create_bus(db, bus)


@router.put("/{bus_id}", response_model=BusResponse)
def edit_bus(
    bus_id: int,
    bus: BusUpdate,
    db: Session = Depends(get_db),
):
    updated = update_bus(db, bus_id, bus)

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Bus not found"
        )

    return updated


@router.delete("/{bus_id}")
def remove_bus(
    bus_id: int,
    db: Session = Depends(get_db),
):
    deleted = delete_bus(db, bus_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Bus not found"
        )

    return {
        "message": "Bus deleted successfully"
    }