from seed import mysession
from models import Dentist, Appointment

def list_dentists():

	mydentist = mysession.query(Dentist).all
	for dentist in mydentist:
		print(dentist.name)
	pass

def date_appointment():
	myappointment = mysession.query(Appointment).all
	for appointment in myappointment:
		print(appointment.date)
	pass
