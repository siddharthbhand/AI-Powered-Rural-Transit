from sqlalchemy import Column, Integer, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database.database import Base


class BusLocation(Base):
    __tablename__ = "bus_locations"

    id = Column(Integer, primary_key=True, index=True)

    bus_id = Column(
        Integer,
        ForeignKey("buses.id", ondelete="CASCADE"),
        nullable=False,
    )

    latitude = Column(Float, nullable=False)

    longitude = Column(Float, nullable=False)

    speed = Column(Float, nullable=True)

    heading = Column(Float, nullable=True)

    recorded_at = Column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    bus = relationship(
        "Bus",
        back_populates="locations",
    )