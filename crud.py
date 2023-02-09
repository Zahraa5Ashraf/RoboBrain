from sqlalchemy.orm import Session
import schemas, models
from fastapi import HTTPException, status, Depends


def store_chair_data(db: Session, data: schemas.ChairData):
    new_data = models.ChairData(
        body_temperature=data.body_temperature,
        oximeter=data.oximeter,
        heart_rate=data.heart_rate,
        sugar_level=data.sugar_level,
        patient_id=data.patient_id,
    )
    patient = (
        db.query(models.Patient).filter(data.patient_id == models.Patient.id).first()
    )
    new_data.patient = patient

    db.add(new_data)
    db.commit()
    db.refresh(new_data)

    return new_data


def get_chair_data(patient_id: int, db: Session):
    db_data = db.query(models.ChairData).filter(models.ChairData.patient_id == patient_id).order_by(models.ChairData.id.desc()).first()
    
    if db_data is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Data not found"
        )
    return db_data


def signup(db: Session, patient: schemas.SignUp):
    db_email = (
        db.query(models.Patient).filter(models.Patient.email == patient.email).first()
    )

    if db_email is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This email is already exist",
        )

    db_username = (
        db.query(models.Patient)
        .filter(models.Patient.username == patient.username)
        .first()
    )

    if db_username is not None:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="This username is already exist",
        )

    new_patient = models.Patient(
        id=patient.id,
        patient_full_name=patient.patient_full_name,
        username=patient.username,
        email=patient.email,
        phone_number=patient.phone_number,
        password=patient.password,
        address=patient.address,
        age=patient.age,
    )

    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)

    return new_patient





# TODO: Complete patient_info CRUD function
def patient_info():
    pass



# TODO: Complete login CRUD function
def login():
    pass

