from models import  Base, Dentist, Patient, Appointment
from faker import Faker
from sqlalchemy import create_engine, null
from sqlalchemy.orm import sessionmaker
import random




engine = create_engine('sqlite:///dentistoffice.db')
Base.metadata.create_all(engine)

sessioncreator = sessionmaker(bind=engine)
mysession = sessioncreator()

fakedata = Faker()
fake = Faker()



print("Seeding for Dentists")
print("Seeding for Patients")
print("Seeding for Appointments")

for i in range(3):
    dentist = Dentist(dentist_name=fakedata.name(), dentist_specialty=null(), patient_id=random.randrange(3))
    mysession.add(dentist)
    mysession.commit()
    


for i in range(10):
    patient = Patient(patient_name=fakedata.name(), dentist_id=random.randrange(10))
    mysession.add(patient)
    mysession.commit()
    

for i in range(10):
    appoinment = Appointment(appointment_date=fake.date_this_month(), appoinment_time=fake.time(), patient_id=random.randrange(10), dentist_id=random.randrange(3))
    mysession.add(appoinment)
    mysession.commit()
    

print('All Seeded Dentists')
print('All Seeded Patients')
print('All Seeded Appointments')
