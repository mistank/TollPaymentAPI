# app/models/toll_payment.py

from pydantic import BaseModel, Field, field_validator
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from sqlalchemy.orm import relationship

from app.db.db import Base


class TollPayment(Base):
    __tablename__ = "toll_payment"

    id = Column(Integer, primary_key=True)
    entry_location_id = Column(Integer,ForeignKey('location.id'), nullable=False)
    exit_location_id = Column(Integer,ForeignKey('location.id'), nullable=False)
    card_number = Column(String(50), nullable=False)
    ccv = Column(String(50), nullable=False)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    toll_price = Column(Float, nullable=False)

    entry_location = relationship("Location",foreign_keys=[entry_location_id],back_populates="entry_toll_payment")
    exit_location = relationship("Location",foreign_keys=[exit_location_id],back_populates="exit_toll_payment")


    def __repr__(self):
        return f"<TollPayment(entry_location={self.entry_location}, exit_location={self.exit_location}, card_number={self.card_number}, ccv={self.ccv}, first_name={self.first_name}, last_name={self.last_name})>"

