from pydantic import BaseModel


class Patient(BaseModel):
    id: int
    patient_name: str
    phone_number: str
    address: str
    age: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "id": 1,
                "patient_name": "Mohamed Ali",
                "phone_number": "0111122234",
                "address": "Zagazig, Egypt",
                "age": 25,
            }
        }


class ChairData(BaseModel):
    body_temperature: float
    oximeter: float
    heart_rate: float
    sugar_level: float
    patient_id: int

    class Config:
        orm_mode = True
        schema_extra = {
            "example": {
                "body_temperature": 36.5,
                "oximeter": 125.4,
                "heart_rate": 122.5,
                "sugar_level": 70.45,
                "patient_id": 1,
            }
        }
