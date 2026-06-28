from sqlalchemy.orm import Session

from app.services.bus_service import BusService
from app.services.bus_location_service import BusLocationService


class PassengerService:

    @staticmethod
    def get_live_buses(
        db: Session,
    ):

        buses = BusService.get_all_buses(db)

        result = []

        for bus in buses:

            latest_location = BusLocationService.get_latest_location(
                db=db,
                bus_id=bus.id,
            )

            result.append(
                {
                    "id": bus.id,
                    "bus_number": bus.bus_number,
                    "bus_name": bus.bus_name,
                    "source": bus.source,
                    "destination": bus.destination,
                    "operator_name": bus.operator_name,
                    "bus_type": bus.bus_type,
                    "status": bus.status,
                    "live_location": (
                        {
                            "latitude": latest_location.latitude,
                            "longitude": latest_location.longitude,
                            "speed": latest_location.speed,
                            "heading": latest_location.heading,
                        }
                        if latest_location
                        else None
                    ),
                }
            )

        return result

    @staticmethod
    def search_buses(
        db: Session,
        source: str,
        destination: str,
    ):

        buses = BusService.search_buses(
            db=db,
            source=source,
            destination=destination,
        )

        result = []

        for bus in buses:

            latest_location = BusLocationService.get_latest_location(
                db=db,
                bus_id=bus.id,
            )

            result.append(
                {
                    "id": bus.id,
                    "bus_number": bus.bus_number,
                    "bus_name": bus.bus_name,
                    "source": bus.source,
                    "destination": bus.destination,
                    "operator_name": bus.operator_name,
                    "bus_type": bus.bus_type,
                    "status": bus.status,
                    "live_location": (
                        {
                            "latitude": latest_location.latitude,
                            "longitude": latest_location.longitude,
                            "speed": latest_location.speed,
                            "heading": latest_location.heading,
                        }
                        if latest_location
                        else None
                    ),
                }
            )

        return result