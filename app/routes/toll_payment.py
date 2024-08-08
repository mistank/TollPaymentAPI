from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app.db.models.toll_payment import TollPayment
from app.db.db import engine, SessionLocal
from app.db.models import toll_payment as toll_payment_model
from app.db.models import location as location_model
from app.db.models import price as price_model

from app.db.schemas import toll_payment as schema

router = APIRouter()
toll_payment_model.Base.metadata.create_all(bind=engine)
location_model.Base.metadata.create_all(bind=engine)
price_model.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@router.post("/pay-toll", response_model=schema.TollPayment)
async def pay_toll(payment: schema.TollPaymentBase, db: Session = Depends(get_db)):
    # Procesuirati placanje
    try:
        if process_payment(payment):
            # kreiranje toll payment objekat u bazi
            # izvuci cenu za put od entry_location do exit_location
            entry_location = db.query(location_model.Location).filter(
                location_model.Location.city == payment.entry_location.city).first()
            exit_location = db.query(location_model.Location).filter(
                location_model.Location.city == payment.exit_location.city).first()
            if (entry_location is None or exit_location is None):
                raise HTTPException(status_code=404, detail="Location not found")
            price = db.query(price_model.Price).filter(price_model.Price.entry_location_id == entry_location.id,
                                                       price_model.Price.exit_location_id == exit_location.id).first()
            db_payment = toll_payment_model.TollPayment(entry_location_id=entry_location.id,
                                                        exit_location_id=exit_location.id,
                                                        card_number=payment.card_number, ccv=payment.ccv,
                                                        first_name=payment.first_name, last_name=payment.last_name,
                                                        toll_price=price.price)
            db.add(db_payment)
            db.commit()
            db.refresh(db_payment)
            return db_payment
        else:
            raise HTTPException(status_code=400, detail="Payment processing failed")
    except ValidationError as e:
        raise HTTPException(status_code=400, detail=e.errors())
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


def process_payment(payment: TollPayment) -> bool:
    # Dodati logiku za procesuiranje placanja
    return True