from datetime import datetime, UTC


class EventBuilder:

    @staticmethod
    def build_location_event(
        bus_id: int,
        latitude: float,
        longitude: float,
        speed: float,
        heading: float,
        distance_km: float,
        eta_minutes: int,
    ):

        return {
            "event": "location_updated",
            "timestamp": datetime.now(UTC).isoformat(),
            "data": {
                "bus_id": bus_id,
                "latitude": latitude,
                "longitude": longitude,
                "speed": speed,
                "heading": heading,
                "distance_km": distance_km,
                "eta_minutes": eta_minutes,
            },
        }