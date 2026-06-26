from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func

from app.database.database import Base


class Route(Base):
    __tablename__ = "routes"

    id = Column(Integer, primary_key=True, index=True)

    route_name = Column(String, nullable=False)

    source = Column(String, nullable=False)

    destination = Column(String, nullable=False)

    distance_km = Column(Integer, nullable=False)

    estimated_time = Column(String, nullable=False)

    status = Column(String, default="Active")

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )