from fastapi import FastAPI
from database import engine, SessionLocal
from models import Base
from chair import router as chair_router
from patient import router as patient_router

# * Here is the main file that will be used to run the application
# Hello i'm editing

app = FastAPI()

# * Create the database tables
Base.metadata.create_all(bind=engine)

# * Include the routers from the other files in the main file to be used by the application
app.include_router(chair_router)
app.include_router(patient_router)
