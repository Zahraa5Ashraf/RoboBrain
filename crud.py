from sqlalchemy.orm import Session
import schemas, models


def store_chair_data(db: Session, data: schemas.ChairData):
    new_data = models.Patient(
        body_temperature=data.body_temperature,
        oximeter=data.oximeter,
        help_rate=data.heart_rate,
        sugar_level=data.sugar_level,
        patient_id=data.patient_id,
    )
    db.add(new_data)
    db.commit()
    db.refresh(new_data)

    return new_data


def get_chair_data(db: Session):
    return db.query(models.ChairData).order_by(models.ChairData.id.desc()).first()


def store_patient_data(db: Session, patient: schemas.Patient):
    new_patient = models.Patient(
        id=patient.patient_id,
        patient_name=patient.patient_name,
        phone_number=patient.phone_number,
        address=patient.address,
        age=patient.age,
    )
    db.add(new_patient)
    db.commit()
    db.refresh(new_patient)
    
    return new_patient
