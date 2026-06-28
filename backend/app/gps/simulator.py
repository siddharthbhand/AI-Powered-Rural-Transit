import asyncio

from app.core.config import settings
from app.database.database import SessionLocal
from app.services.gps_service import GPSService


class GPSSimulator:

    def __init__(self, bus_id: int):

        self.bus_id = bus_id

        self.latitude = 18.5204 + (bus_id * 0.002)
        self.longitude = 73.8567 + (bus_id * 0.002)

        self.speed = settings.DEFAULT_SPEED
        self.heading = settings.DEFAULT_HEADING

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
                    bus_id=self.bus_id,
                    latitude=location["latitude"],
                    longitude=location["longitude"],
                    speed=self.speed,
                    heading=self.heading,
                )

                print("=" * 60)
                print(f"Bus {self.bus_id} GPS Saved")
                print(location)
                print(f"Speed: {self.speed} km/h")
                print(f"Heading: {self.heading}")
                print("=" * 60)

            finally:

                db.close()

            await asyncio.sleep(
                settings.GPS_UPDATE_INTERVAL
            )