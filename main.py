from fastapi import FastAPI
from database import engine
from models import Base
from chair import router as chair_router
from patient import router as patient_router


app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(chair_router)
app.include_router(patient_router)