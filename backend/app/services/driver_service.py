from sqlalchemy.orm import Session

from app.services.gps_service import GPSService


class DriverService:

    @staticmethod
    async def update_driver_location(
        db: Session,
        bus_id: int,
        latitude: float,
        longitude: float,
        speed: float,
        heading: float,
    ):

        return await GPSService.save_location(
            db=db,
            bus_id=bus_id,
            latitude=latitude,
            longitude=longitude,
            speed=speed,
            heading=heading,
        )