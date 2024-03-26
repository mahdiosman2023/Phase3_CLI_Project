from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, create_engine, engine


Base = declarative_base()

class Dentist(Base):

    def __init__(self, id, dentis_name, dentist_specialty):
        self.id = id
        self.dentist_name = dentis_name
        self.dentist_specialty = dentist_specialty
    
    __tablename__ = "dentists"  
    
    id = Column(Integer(), primary_key=True)
    dentist_name = Column(String())
    dentist_specialty = Column(String())

    #patients = relationship("Patient", backref="dentist")


class Patient(Base):

    __tablename__ = "patients"  

    id = Column(Integer, primary_key=True)
    patient_name = Column(String())
    procedure = Column(String())
    dentist_id = Column(Integer(), ForeignKey("dentists.id"))


class Appointment(Base):

    __tablename__ = "appointments"  # Corrected typo

    id = Column(Integer(), primary_key=True)
    appointment_date = Column(Integer())
    appoinment_time = Column(Integer())
    patient_id = Column(Integer, ForeignKey("patients.id"))
    dentist_id = Column(Integer, ForeignKey("dentists.id"))



if __name__ == "__main__":
engine = create_engine("sqlite:///dentist.db")
session = Session(engine, future=True)
Cli()