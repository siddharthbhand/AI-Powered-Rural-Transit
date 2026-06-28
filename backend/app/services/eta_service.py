from app.eta.calculator import ETACalculator


class ETAService:

    @staticmethod
    def calculate_eta(
        start_lat: float,
        start_lon: float,
        end_lat: float,
        end_lon: float,
        speed: float,
    ):

        distance = ETACalculator.calculate_distance(
            start_lat,
            start_lon,
            end_lat,
            end_lon,
        )

        eta = ETACalculator.calculate_eta(
            distance,
            speed,
        )

        return {
            "distance_km": distance,
            "speed_kmh": speed,
            "eta_minutes": eta,
        }