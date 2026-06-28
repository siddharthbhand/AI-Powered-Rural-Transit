from sqlalchemy.orm import Session

from app.models.bus import Bus
from app.models.bus_location import BusLocation
from app.schemas.bus_location import (
    BusLocationCreate,
    BusLocationUpdate,
)


class BusLocationService:

    @staticmethod
    def create_location(
        db: Session,
        location: BusLocationCreate,
    ):

        bus = db.query(Bus).filter(
            Bus.id == location.bus_id
        ).first()

        if not bus:
            return None

        db_location = BusLocation(**location.model_dump())

        db.add(db_location)
        db.commit()
        db.refresh(db_location)

        return db_location

    @staticmethod
    def get_all_locations(
        db: Session,
    ):

        return db.query(BusLocation).all()

    @staticmethod
    def get_location_by_id(
        db: Session,
        location_id: int,
    ):

        return db.query(BusLocation).filter(
            BusLocation.id == location_id
        ).first()

    @staticmethod
    def get_locations_by_bus(
        db: Session,
        bus_id: int,
    ):

        return db.query(BusLocation).filter(
            BusLocation.bus_id == bus_id
        ).all()

    @staticmethod
    def get_latest_location(
        db: Session,
        bus_id: int,
    ):

        return (
            db.query(BusLocation)
            .filter(
                BusLocation.bus_id == bus_id
            )
            .order_by(
                BusLocation.recorded_at.desc()
            )
            .first()
        )

    @staticmethod
    def update_location(
        db: Session,
        location_id: int,
        location: BusLocationUpdate,
    ):

        db_location = db.query(BusLocation).filter(
            BusLocation.id == location_id
        ).first()

        if not db_location:
            return None

        update_data = location.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(db_location, key, value)

        db.commit()
        db.refresh(db_location)

        return db_location

    @staticmethod
    def delete_location(
        db: Session,
        location_id: int,
    ):

        db_location = db.query(BusLocation).filter(
            BusLocation.id == location_id
        ).first()

        if not db_location:
            return None

        db.delete(db_location)
        db.commit()

        return db_location