from math import radians, sin, cos, sqrt, atan2


class ETACalculator:

    @staticmethod
    def calculate_distance(
        start_lat: float,
        start_lon: float,
        end_lat: float,
        end_lon: float,
    ) -> float:

        earth_radius = 6371

        lat1 = radians(start_lat)
        lon1 = radians(start_lon)

        lat2 = radians(end_lat)
        lon2 = radians(end_lon)

        delta_lat = lat2 - lat1
        delta_lon = lon2 - lon1

        a = (
            sin(delta_lat / 2) ** 2
            + cos(lat1)
            * cos(lat2)
            * sin(delta_lon / 2) ** 2
        )

        c = 2 * atan2(
            sqrt(a),
            sqrt(1 - a),
        )

        distance = earth_radius * c

        return round(distance, 2)

    @staticmethod
    def calculate_eta(
        distance: float,
        speed: float,
    ) -> int:

        if speed <= 0:
            return 0

        eta_hours = distance / speed

        eta_minutes = eta_hours * 60

        return round(eta_minutes)