from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import schemas, database, crud, models

router = APIRouter(tags=["patient"], prefix="/patient")

models.Base.metadata.create_all(bind=database.engine)


@router.post(
    "/info", response_model=schemas.Patient, status_code=status.HTTP_201_CREATED
)
async def store_patient_info(
    patient: schemas.Patient, db: Session = Depends(database.get_db)
):
    return crud.store_patient_data(db=db, patient=patient)
