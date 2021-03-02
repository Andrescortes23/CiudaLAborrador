import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "CuidaLA.settings")
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from Database.models import User, Locations, Jobs, Applicants, Skills
from datetime import datetime


#LOCATIONS
#Cities = ['Cali', 'Bogotá', 'Ipiales', 'Pereira']
#for city in Cities:
#    the_city=Locations(name=city)
#    the_city.save()

#SKILLS
The_Skills=[]

#USER
#Newuser=User(first_name=input("Introduzca su nombre: "), last_name=input("Introduzca su apellido: "),
#legal_id=input("Introduzca su Númer de Cédula: "), email=input("Mail: "), password=input("Password: "),
#caregiver=input("True si es cuidador: "), patient=input("True si eres paciente: "), adress=input("Dirección: "),
#phone=input("Cel: "), created_at=datetime.now().strftime('%Y-%m-%d'), updated_at=datetime.now().strftime('%Y-%m-%d'),
#location_id=Locations.objects.get(name=input("Ciudad: ")))
#Newuser.save()
#print(Newuser)

#JOBS
#Newjob=Jobs(the_type=input("Cuidados Especiales\nCompañia\nCuidado Adulto Mayor\nTipo de trabajo: "), created_at=datetime.now().strftime('%Y-%m-%d'),
#tart_date=datetime.now().strftime('%Y-%m-%d'), end_date=datetime.now().strftime('%Y-%m-%d'),
#patient_phone=User.objects.get(first_name="Andres").phone, patient_age=27,
#user_id=User.objects.get(first_name="Andres"), salary_start=50000, salary_end=60000,
#status="Taken", updated_at=datetime.now().strftime('%Y-%m-%d'),
#location_id=User.objects.get(first_name="Andres").location_id.id)
#Newjob.save()
#print(Newjob.location_id)

#APPLICANT
#New_applicant=Applicants(job_id=Jobs.objects.get(id=3), caregiver_offer=50000, patient_offer=60000,
#status=("Available" if Jobs.objects.get(status="Taken") else "Not Avlb"),
#created_at=datetime.now().strftime('%Y-%m-%d'), updated_at=datetime.now().strftime('%Y-%m-%d'))
#New_applicant.save()
