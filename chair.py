from fastapi import APIRouter, HTTPException, status, Depends
import database, schemas, crud
from sqlalchemy.orm import Session


router = APIRouter(
    tags=["chair"],
    prefix="/chair",
)


@router.get(
    "/data", response_model=list[schemas.ChairData], status_code=status.HTTP_200_OK
)
async def get_chair_data(db: Session = Depends(database.get_db)):
    return crud.get_chair_data(db=db)


@router.post(
    "/data", response_model=schemas.ChairData, status_code=status.HTTP_202_ACCEPTED
)
async def read_new_chair_data(
    data: schemas.ChairData, db: Session = Depends(database.get_db)
):
    return crud.store_chair_data(data=data, db=db)
