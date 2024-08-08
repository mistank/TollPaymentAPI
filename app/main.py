import uvicorn
from fastapi import FastAPI

from app.db.db import Base, engine
from app.routes import toll_payment

app = FastAPI()
Base.metadata.create_all(bind=engine)

app.include_router(toll_payment.router, tags=["toll_payment"])

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello my {name}"}


# Pokretanje aplikacije sa uvicorn serverom
if __name__ == "__main__":
    print("Starting the server")
    uvicorn.run(app, host="127.0.0.1", port=8000)