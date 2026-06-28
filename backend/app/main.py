import asyncio
from fastapi import FastAPI

print("========== MAIN.PY LOADED ==========")
print("GPS STARTUP IS DISABLED")

from app.api.auth import router as auth_router
from app.api.bus import router as bus_router
from app.api.route import router as route_router
from app.api.bus_location import router as bus_location_router
from app.api.eta import router as eta_router
from app.api.driver import router as driver_router
from app.websocket.websocket import router as websocket_router

from app.gps.manager import GPSSimulationManager


app = FastAPI()

gps_manager = GPSSimulationManager()


#@app.on_event("startup")
#async def start_gps_simulation():

#    asyncio.create_task(
 #       gps_manager.start()
  #  )


app.include_router(auth_router)
app.include_router(bus_router)
app.include_router(route_router)
app.include_router(bus_location_router)
app.include_router(eta_router)
app.include_router(driver_router)
app.include_router(websocket_router)


@app.get("/")
def home():

    return {
        "message": "Hello Siddharth"
    }