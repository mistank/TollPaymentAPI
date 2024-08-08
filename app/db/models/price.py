from sqlalchemy import Column, Float, String, ForeignKey, Integer
from sqlalchemy.orm import relationship

from app.db.db import Base


class Price(Base):
    __tablename__ = "price"

    price_id = Column(Integer, primary_key=True)
    entry_location_id = Column(Integer, ForeignKey('location.id'))
    exit_location_id = Column(Integer, ForeignKey('location.id'))
    price = Column(Float, nullable=False)

    entry_location = relationship("Location", foreign_keys=[entry_location_id])
    exit_location = relationship("Location", foreign_keys=[exit_location_id])

    def __repr__(self):
        return f"<Price(entry_location_id={self.entry_location_id}, exit_location_id={self.exit_location_id}, price={self.price})>"

    @staticmethod
    def validate_locations(entry_location_id, exit_location_id):
        if entry_location_id == exit_location_id:
            raise ValueError("Entry location and exit location must be different.")