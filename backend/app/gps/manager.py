import asyncio

from app.core.config import settings
from app.gps.simulator import GPSSimulator


class GPSSimulationManager:

    def __init__(self):

        self.simulators = []

    async def start(self):

        tasks = []

        for bus_id in range(
            1,
            settings.DEFAULT_BUS_ID + 1,
        ):

            simulator = GPSSimulator(bus_id)

            self.simulators.append(simulator)

            tasks.append(
                asyncio.create_task(
                    simulator.start()
                )
            )

        await asyncio.gather(*tasks)