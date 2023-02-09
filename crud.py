from sqlalchemy.orm import Session
import schemas, models
from fastapi import HTTPException, status


def store_chair_data(db: Session, data: schemas.ChairData):
    new_data = models.ChairData(
        body_temperature=data.body_temperature,
        oximeter=data.oximeter,
        heart_rate=data.heart_rate,
        sugar_level=data.sugar_level,
        patient_id=data.patient_id,  
    )
    patient = db.query(models.Patient).filter(data.patient_id == models.Patient.id).first()
    new_data.patient = patient
    
    db.add(new_data)
    db.commit()
    db.refresh(new_data)

    return new_data


def get_chair_data(db: Session):
    return db.query(models.ChairData).order_by(models.ChairData.id.desc()).first()


def store_patient_data(db: Session, patient: schemas.Patient):
    
    
    
    new_patient = models.Patient(
        id = patient.id,
        patient_name=patient.patient_name,
        phone_number=patient.phone_number,
        address=patient.address,
        age=patient.age,
    )
    
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    
    return new_patient
