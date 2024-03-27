from models import  Base, Dentist, Patient, Appointment
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



engine = create_engine('sqlite:///dentistoffice.db')
Base.metadata.create_all(engine)

sessioncreator = sessionmaker(bind=engine)
mysession = sessioncreator()

fakedata = Faker()

print("Seeding for Dentists")
print("Seeding for Patients")
print("Seeding for Appointments")

for i in range(3):
    dentist = Dentist(name=fakedata.name())
    mysession.add(dentist)
mysession.commit()

for i in range(10):
    paitient = Patient(name=fakedata.name())
    procedure = procedure(name=fakedata.name())
    mysession.add(paitient)
    mysession.add(procedure)

mysession.commit()

for i in range(10):
    appoinment = Appointment(date=fakedata.date())
    mysession.add(appoinment)
mysession.commit()

print('All Seeded Dentists')
print('All Seeded Patients')
print('All Seeded Appointments')