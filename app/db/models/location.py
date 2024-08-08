from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

from app.db.db import Base


class Location(Base):
    __tablename__ = "location"

    id = Column(Integer, primary_key=True)
    city = Column(String(50), nullable=False)

    entry_toll_payment = relationship("TollPayment", foreign_keys="[TollPayment.entry_location_id]", back_populates="entry_location")
    exit_toll_payment = relationship("TollPayment", foreign_keys="[TollPayment.exit_location_id]",back_populates="exit_location")
    entry_prices = relationship("Price", foreign_keys="[Price.entry_location_id]", back_populates="entry_location")
    exit_prices = relationship("Price", foreign_keys="[Price.exit_location_id]", back_populates="exit_location")

    def __repr__(self):
        return f"<Location(name={self.name}, address={self.address}, city={self.city}, country={self.country})>"