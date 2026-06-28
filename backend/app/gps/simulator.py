import asyncio

from app.database.database import SessionLocal
from app.services.gps_service import GPSService


class GPSSimulator:

    def __init__(self):

        self.latitude = 18.5204
        self.longitude = 73.8567

    def move_bus(self):

        self.latitude += 0.0001
        self.longitude += 0.0001

        return {
            "latitude": self.latitude,
            "longitude": self.longitude,
        }

    async def start(self):

        while True:

            location = self.move_bus()

            db = SessionLocal()

            try:

                await GPSService.save_location(
                    db=db,
                    bus_id=2,
                    latitude=location["latitude"],
                    longitude=location["longitude"],
                )

                print("=" * 50)
                print("GPS Saved")
                print(location)
                print("=" * 50)

            finally:

                db.close()

            await asyncio.sleep(3)