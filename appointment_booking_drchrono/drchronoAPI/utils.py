import datetime

from drchronoAPI.api import get_doctors, get_offices, get_patients
from drchronoAPI.models import Doctor, Office, Patient


# TODO make these generic
def update_doctors_for_user(user):
    parameters = {}
    doctors = get_doctors(user, parameters)
    for d in doctors:
        doctor, created = Doctor.objects.update_or_create(
            id=d['id'],
            defaults= {
                'user': user,
                'first_name': d['first_name'],
                'last_name': d['last_name'],
                'suffix': d['suffix'],
                'job_title': d['job_title'],
                'specialty': d['specialty'],
                'cell_phone': d['cell_phone'],
                'home_phone': d['home_phone'],
                'office_phone': d['office_phone'],
                'email': d['email'],
                'website': d['website'],
            },
        )

def update_offices_for_user(user):
    parameters = {}
    offices = get_offices(user, parameters)
    for o in offices:
        office, created = Office.objects.update_or_create(
            id=o['id'],
            defaults= {
                'user': user,
                'online_scheduling': o['online_scheduling'],
                'online_timeslots': o.get('online_timeslots',''),
                'address': o['address'],
                'city': o['city'],
                'country': o['country'],
                'name': o['name'],
                'state': o['state'],
                'zip_code': o['zip_code'],
                'doctor': o['doctor'],
                'end_time': o['end_time'],
                'phone_number': o['phone_number'],
                'start_time': o['start_time'],
                # TODO: add exam room model
                #'exam_rooms': o['exam_rooms'],
                'id': o['id'],
            },
        )

def update_patients_for_user(user, last_ran=None):
    parameters = {}
    if last_ran:
        parameters['since'] = last_ran
    patients = get_patients(user, parameters)
    for p in patients:
        date_of_birth = p['date_of_birth']
        if date_of_birth:
            year, month, day = [int(x) for x in p['date_of_birth'].split('-')]
            date_of_birth = datetime.date(year, month, day)
            patient, created = Patient.objects.update_or_create(
                id=p['id'],
                defaults= {
                    'user': user,
                    'date_of_birth': date_of_birth,
                    'doctor': p['doctor'],
                    'first_name': p['first_name'],
                    'last_name': p['last_name'],
                    'cell_phone': p['cell_phone'],
                    'email': p['email'],
                    'state': p['state'],
                },
            )
