from models import Base, Dentist, Patient, Appointment
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Create the engine
engine = create_engine('sqlite:///dentistoffice.db')

# Create all tables
Base.metadata.create_all(engine)

# Create a sessionmaker
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

# Create a Faker instance
fake = Faker()

# Seeding Dentists
print("Seeding for Dentists")
for _ in range(3):
    dentist = Dentist(name=fake.name())
    session.add(dentist)
session.commit()
print('All Dentists Seeded')

# Seeding Patients
print("Seeding for Patients")
for _ in range(10):
    patient = Patient(name=fake.name())
    session.add(patient)
session.commit()
print('All Patients Seeded')

# Seeding Appointments
print("Seeding for Appointments")
for _ in range(10):
    appointment = Appointment(date=fake.date())
    session.add(appointment)
session.commit()
print('All Appointments Seeded')

# Close the session
session.close()
