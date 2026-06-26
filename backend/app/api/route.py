from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.schemas.route import (
    RouteCreate,
    RouteUpdate,
    RouteResponse,
)

from app.services.route_service import (
    create_route,
    get_routes,
    get_route,
    update_route,
    delete_route,
)

router = APIRouter(
    prefix="/routes",
    tags=["Route Management"],
)


@router.post("/", response_model=RouteResponse)
def add_route(route: RouteCreate, db: Session = Depends(get_db)):
    return create_route(db, route)


@router.get("/", response_model=list[RouteResponse])
def all_routes(db: Session = Depends(get_db)):
    return get_routes(db)


@router.get("/{route_id}", response_model=RouteResponse)
def single_route(route_id: int, db: Session = Depends(get_db)):
    route = get_route(db, route_id)

    if not route:
        raise HTTPException(
            status_code=404,
            detail="Route not found"
        )

    return route


@router.put("/{route_id}", response_model=RouteResponse)
def edit_route(
    route_id: int,
    route: RouteUpdate,
    db: Session = Depends(get_db)
):
    updated = update_route(db, route_id, route)

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Route not found"
        )

    return updated


@router.delete("/{route_id}")
def remove_route(route_id: int, db: Session = Depends(get_db)):
    deleted = delete_route(db, route_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Route not found"
        )

    return {
        "message": "Route deleted successfully"
    }