from sqlalchemy.orm import Session

from app.core.config import settings
from app.schemas.bus_location import BusLocationCreate
from app.services.bus_location_service import BusLocationService
from app.services.eta_service import ETAService
from app.utils.event_builder import EventBuilder
from app.websocket.websocket import connection_manager


class GPSService:

    @staticmethod
    async def save_location(
        db: Session,
        bus_id: int,
        latitude: float,
        longitude: float,
        speed: float,
        heading: float,
    ):

        location = BusLocationCreate(
            bus_id=bus_id,
            latitude=latitude,
            longitude=longitude,
            speed=speed,
            heading=heading,
        )

        saved_location = BusLocationService.create_location(
            db,
            location,
        )

        if not saved_location:
            return None

        eta = ETAService.calculate_eta(
            start_lat=latitude,
            start_lon=longitude,
            end_lat=settings.DESTINATION_LATITUDE,
            end_lon=settings.DESTINATION_LONGITUDE,
            speed=speed,
        )

        event = EventBuilder.build_location_event(
            bus_id=bus_id,
            latitude=latitude,
            longitude=longitude,
            speed=speed,
            heading=heading,
            distance_km=eta["distance_km"],
            eta_minutes=eta["eta_minutes"],
        )

        await connection_manager.broadcast_event(event)

        return saved_location