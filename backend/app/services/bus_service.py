from sqlalchemy.orm import Session

from app.models.bus import Bus
from app.schemas.bus import BusCreate, BusUpdate


class BusService:

    @staticmethod
    def get_all_buses(db: Session):
        return db.query(Bus).all()

    @staticmethod
    def get_bus_by_id(db: Session, bus_id: int):
        return db.query(Bus).filter(Bus.id == bus_id).first()

    @staticmethod
    def get_bus_by_number(db: Session, bus_number: str):
        return db.query(Bus).filter(Bus.bus_number == bus_number).first()

    @staticmethod
    def create_bus(db: Session, bus: BusCreate):
        db_bus = Bus(
            bus_number=bus.bus_number,
            bus_name=bus.bus_name,
            operator_name=bus.operator_name,
            source=bus.source,
            destination=bus.destination,
            total_seats=bus.total_seats,
            available_seats=bus.available_seats,
            bus_type=bus.bus_type,
            status=bus.status,
        )

        db.add(db_bus)
        db.commit()
        db.refresh(db_bus)

        return db_bus

    @staticmethod
    def update_bus(
        db: Session,
        bus_id: int,
        bus: BusUpdate,
    ):

        db_bus = BusService.get_bus_by_id(
            db,
            bus_id,
        )

        if not db_bus:
            return None

        db_bus.bus_number = bus.bus_number
        db_bus.bus_name = bus.bus_name
        db_bus.operator_name = bus.operator_name
        db_bus.source = bus.source
        db_bus.destination = bus.destination
        db_bus.total_seats = bus.total_seats
        db_bus.available_seats = bus.available_seats
        db_bus.bus_type = bus.bus_type
        db_bus.status = bus.status

        db.commit()
        db.refresh(db_bus)

        return db_bus

    @staticmethod
    def delete_bus(
        db: Session,
        bus_id: int,
    ):

        db_bus = BusService.get_bus_by_id(
            db,
            bus_id,
        )

        if not db_bus:
            return None

        db.delete(db_bus)
        db.commit()

        return db_bus

    @staticmethod
    def get_live_buses_by_route(
        db: Session,
        source: str,
        destination: str,
    ):

        return (
            db.query(Bus)
            .filter(
                Bus.source == source,
                Bus.destination == destination,
                Bus.status == "Active",
            )
            .all()
        )

    @staticmethod
    def search_buses(
        db: Session,
        source: str,
        destination: str,
    ):

        return (
            db.query(Bus)
            .filter(
                Bus.source.ilike(source),
                Bus.destination.ilike(destination),
            )
            .all()
        )