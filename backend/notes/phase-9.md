# Phase 9 – Passenger Module and Real-Time ETA

## Objective

Build the Passenger Module so that passengers can:

- View all live buses
- Search buses by route
- View bus details
- Track live GPS location
- See remaining distance
- See estimated arrival time (ETA)

---

# Features Implemented

## 1. Live Buses API

Endpoint

GET /passenger/live-buses

Features

- Returns all active buses
- Returns latest GPS location
- Returns operator information
- Returns bus status
- Returns remaining distance
- Returns ETA
- Returns average speed

---

## 2. Search Buses API

Endpoint

GET /passenger/search

Query Parameters

- source
- destination

Features

- Search buses by source
- Search buses by destination
- Live GPS integration
- ETA calculation
- Remaining distance calculation

---

## 3. Bus Details API

Endpoint

GET /passenger/bus/{bus_id}

Features

- Bus information
- Live GPS location
- Operator details
- Remaining distance
- ETA
- Average speed

---

## 4. Passenger Service

Created

app/services/passenger_service.py

Responsibilities

- Fetch live buses
- Search buses
- Fetch bus details
- Integrate Bus Service
- Integrate GPS Service
- Integrate ETA Service

---

## 5. ETA Integration

Integrated

app/services/eta_service.py

Output

- Distance Remaining
- ETA (Minutes)
- Average Speed

---

## 6. City Coordinate Mapping

Created

app/utils/city_coordinates.py

Purpose

Maps destination city names to GPS coordinates.

Example

Pune

Latitude: 18.5204

Longitude: 73.8567

Mumbai

Latitude: 19.0760

Longitude: 72.8777

This utility is reusable across:

- Passenger APIs
- ETA calculation
- Maps
- Future route visualization

---

## APIs Tested

Successfully tested in Swagger

✓ GET /passenger/live-buses

✓ GET /passenger/search

✓ GET /passenger/bus/{bus_id}

All APIs returned

200 OK

---

## Project Structure Added

app/

├── services/

│ └── passenger_service.py

├── utils/

│ └── city_coordinates.py

---

## Git Commit

Commit Message

Phase 9.5 completed - Real ETA and distance integration

---

## Key Learnings

- Service-to-service communication
- ETA calculation
- Haversine distance calculation
- Modular backend architecture
- Utility module creation
- Real-time passenger APIs
- GPS data integration
- Clean service layer implementation

---

## Production Improvements

Implemented

✓ Modular services

✓ Reusable utility

✓ Clean architecture

✓ No duplicate logic

✓ Separation of concerns

✓ Real ETA integration

---

## Phase Status

Phase 9

COMPLETED

Status

Production Ready