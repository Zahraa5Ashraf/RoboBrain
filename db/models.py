from sqlalchemy import Column, String, Integer, Float, ForeignKey, Date, Enum
from sqlalchemy.orm import relationship
from database import Base


class Relation(str, Enum):
    family = "family"
    friend = "friend"
    neighbour = "neighbour"


class Patient(Base):
    __tablename__ = "patient"

    id = Column(Integer, primary_key=True, index=True)
    patient_name = Column(String, nullable=False, index=True)
    phone_number = Column(String, nullable=False, index=True)
    address = Column(String)
    birth_date = Column(Date)

    caregiver = relationship("Caregiver", back_populates="patient")
    chair_data = relationship("ChairData", back_populates="patient")


class Caregiver(Base):
    __tablename__ = "caregiver"

    id = Column(Integer, primary_key=True, index=True)
    caregiver_name = Column(String, nullable=False, index=True)
    phone_number = Column(String, nullable=False, index=True)
    address = Column(String)
    relation = Column(Relation)

    patient_id = Column(Integer, ForeignKey("patient.id"))
    paitent = relationship("Patient", back_population="caregiver")


class ChairData(Base):
    __tablename__ = "chair data"

    chair_id = Column(Integer, primary_key=True, index=True)
    body_temperature = Column(Float, nullable=False)
    oximeter = Column(Float, nullable=False)
    heart_rate = Column(Float, nullable=False)
    suger_level = Column(Float, nullable=False)

    patient_id = Column(Integer, ForeignKey("patient.id"))
    patient = relationship("Patient", back_populates="chair")
