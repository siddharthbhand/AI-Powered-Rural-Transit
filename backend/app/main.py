from fastapi import FastAPI
from app.api.auth import router as auth_router
from app.api.bus import router as bus_router
from app.api.route import router as route_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(bus_router)
app.include_router(route_router)

@app.get("/")
def home():
    return {"message": "Hello Siddharth"}