from sqlalchemy.orm import Session

from app.services.bus_service import BusService
from app.services.bus_location_service import BusLocationService
from app.services.eta_service import ETAService
from app.utils.city_coordinates import CITY_COORDINATES


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

            eta_data = None

            if latest_location:

                destination_coordinates = CITY_COORDINATES.get(
                    bus.destination
                )

                if destination_coordinates:

                    eta_data = ETAService.calculate_eta(
                        start_lat=latest_location.latitude,
                        start_lon=latest_location.longitude,
                        end_lat=destination_coordinates["latitude"],
                        end_lon=destination_coordinates["longitude"],
                        speed=latest_location.speed,
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

                    "distance_remaining_km": (
                        eta_data["distance_km"]
                        if eta_data
                        else None
                    ),

                    "eta_minutes": (
                        eta_data["eta_minutes"]
                        if eta_data
                        else None
                    ),

                    "average_speed": (
                        eta_data["speed_kmh"]
                        if eta_data
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

            eta_data = None

            if latest_location:

                destination_coordinates = CITY_COORDINATES.get(
                    bus.destination
                )

                if destination_coordinates:

                    eta_data = ETAService.calculate_eta(
                        start_lat=latest_location.latitude,
                        start_lon=latest_location.longitude,
                        end_lat=destination_coordinates["latitude"],
                        end_lon=destination_coordinates["longitude"],
                        speed=latest_location.speed,
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

                    "distance_remaining_km": (
                        eta_data["distance_km"]
                        if eta_data
                        else None
                    ),

                    "eta_minutes": (
                        eta_data["eta_minutes"]
                        if eta_data
                        else None
                    ),

                    "average_speed": (
                        eta_data["speed_kmh"]
                        if eta_data
                        else None
                    ),
                }
            )

        return result