from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import schemas, database, crud, models

router = APIRouter(tags=["patient"], prefix="/patient")

models.Base.metadata.create_all(bind=database.engine)

@router.post("/signup", response_model=schemas.SignUp, status_code=status.HTTP_201_CREATED)
async def signup(patient: schemas.SignUp, db: Session = Depends(database.get_db)):
    return crud.signup(patient=patient, db=db)



# TODO: Create 2 Routes
#* POST  ==>  "/login"
#* GET  ==>  "/me"