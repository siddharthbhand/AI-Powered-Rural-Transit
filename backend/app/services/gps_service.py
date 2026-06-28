from sqlalchemy.orm import Session

from app.schemas.bus_location import BusLocationCreate
from app.services.bus_location_service import BusLocationService
from app.websocket.websocket import connection_manager


class GPSService:

    @staticmethod
    async def save_location(
        db: Session,
        bus_id: int,
        latitude: float,
        longitude: float,
    ):

        location = BusLocationCreate(
            bus_id=bus_id,
            latitude=latitude,
            longitude=longitude,
            speed=40,
            heading=180,
        )

        saved_location = BusLocationService.create_location(
            db,
            location,
        )

        if saved_location:

            await connection_manager.broadcast(
                f"Bus {bus_id} location updated"
            )

        return saved_location