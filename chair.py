from fastapi import APIRouter, HTTPException, status, Depends
import database, schemas, crud, models
from sqlalchemy.orm import Session


router = APIRouter(
    tags=["chair"],
    prefix="/chair",
)

models.Base.metadata.create_all(bind=database.engine)


@router.get(
    "/data/{patient_id}", status_code=status.HTTP_200_OK
)
async def get_chair_data(patient_id: int, db: Session = Depends(database.get_db)):
    return crud.get_chair_data(patient_id = patient_id, db=db)


@router.post(
    "/data", response_model=schemas.ChairData, status_code=status.HTTP_202_ACCEPTED
)
async def read_new_chair_data(
    data: schemas.ChairData, db: Session = Depends(database.get_db)
):
    return crud.store_chair_data(data=data, db=db)
