from sqlalchemy.orm import Session

from app.models.route import Route
from app.schemas.route import RouteCreate, RouteUpdate


def create_route(db: Session, route: RouteCreate):
    db_route = Route(**route.model_dump())
    db.add(db_route)
    db.commit()
    db.refresh(db_route)
    return db_route


def get_routes(db: Session):
    return db.query(Route).all()


def get_route(db: Session, route_id: int):
    return db.query(Route).filter(Route.id == route_id).first()


def update_route(db: Session, route_id: int, route: RouteUpdate):
    db_route = get_route(db, route_id)

    if not db_route:
        return None

    for key, value in route.model_dump().items():
        setattr(db_route, key, value)

    db.commit()
    db.refresh(db_route)

    return db_route


def delete_route(db: Session, route_id: int):
    db_route = get_route(db, route_id)

    if not db_route:
        return None

    db.delete(db_route)
    db.commit()

    return db_route