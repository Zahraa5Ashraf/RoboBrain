from pydantic import BaseModel

class Patient(BaseModel):
    patient_id: int
    patient_name: str
    phoen_number: str
    address: str 
    
    class Config: 
        orm_mode=True
    
class ChairData(BaseModel):
    chair_id: int
    body_temperature: float
    oximeter: float
    heart_rate: float
    sugar_level: float
    
    patient_id: int
    
    class Config: 
        orm_mode=True