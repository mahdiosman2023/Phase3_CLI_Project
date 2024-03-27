from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, String, Integer, ForeignKey, create_engine


Base = declarative_base()

class Dentist(Base):
    __tablename__ = "dentists"  
    
    id = Column(Integer(), primary_key=True)
    dentist_name = Column(String())
    dentist_specialty = Column(String())
    patient_id = Column(Integer(), ForeignKey("patient.id"))

    patients = relationship("Patient", backref="dentist")
    appointments = relationship("Appoinment", backref="dentist")


class Patient(Base):

    __tablename__ = "patients"  

    id = Column(Integer, primary_key=True)
    patient_name = Column(String())
    procedure = Column(String())
    dentist_id = Column(Integer(), ForeignKey("dentists.id"))

    dentists = relationship("Dentist", backref="patient")
    appointments = relationship("Appointment", backref="patient")


class Appointment(Base):

    __tablename__ = "appointments"  

    id = Column(Integer(), primary_key=True)
    appointment_date = Column(Integer())
    appoinment_time = Column(Integer())
    patient_id = Column(Integer, ForeignKey("patients.id"))
    dentist_id = Column(Integer, ForeignKey("dentists.id"))



if __name__ == '__main__':
    ourengine = create_engine('sqlite:///dentistsoffice.db')
    Base.metadata.create_all(ourengine)




