from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

from app.database.database import Base


class Bus(Base):
    __tablename__ = "buses"

    id = Column(Integer, primary_key=True, index=True)

    bus_number = Column(String, unique=True, nullable=False)
    bus_name = Column(String, nullable=False)

    operator_name = Column(String, nullable=False)

    source = Column(String, nullable=False)
    destination = Column(String, nullable=False)

    total_seats = Column(Integer, nullable=False)
    available_seats = Column(Integer, nullable=False)

    bus_type = Column(String, nullable=False)

    status = Column(String, default="Active")

    created_at = Column(DateTime(timezone=True), server_default=func.now())

    updated_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )

    locations = relationship(
    "BusLocation",
    back_populates="bus",
    cascade="all, delete-orphan"
)