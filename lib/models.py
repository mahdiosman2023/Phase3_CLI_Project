from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, String, Integer, Date, ForeignKey, create_engine


Base = declarative_base()

class Dentist(Base):
    __tablename__ = 'dentists'
    id = Column(Integer, primary_key=True)
    dentist_name = Column(String)
    dentist_specialty = Column(String)
    patient_id = Column(Integer, ForeignKey('patients.id'))
    
    patients = relationship("Patient", foreign_keys=[patient_id])

class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    patient_name = Column(String)
    dentist_id = Column(Integer, ForeignKey('dentists.id'))

    dentist = relationship("Dentist", foreign_keys=[dentist_id])


class Appointment(Base):

    __tablename__ = "appointments"  

    id = Column(Integer(), primary_key=True)
    appointment_date = Column(Date())
    appoinment_time = Column(Integer())
    patient_id = Column(Integer, ForeignKey("patients.id"))
    dentist_id = Column(Integer, ForeignKey("dentists.id"))



if __name__ == '__main__':
    ourengine = create_engine('sqlite:///dentistsoffice.db')
    Base.metadata.create_all(ourengine)




