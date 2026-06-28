from fastapi import FastAPI
import asyncio

from app.gps.simulator import GPSSimulator

from app.api.auth import router as auth_router
from app.api.bus import router as bus_router
from app.api.route import router as route_router
from app.api.bus_location import router as bus_location_router
from app.websocket.websocket import router as websocket_router

app = FastAPI()

gps_simulator = GPSSimulator()

@app.on_event("startup")
async def start_gps_simulator():

    asyncio.create_task(
        gps_simulator.start()
    )

app.include_router(auth_router)
app.include_router(bus_router)
app.include_router(route_router)
app.include_router(bus_location_router)
app.include_router(websocket_router)


@app.get("/")
def home():
    return {
        "message": "Hello Siddharth"
    }