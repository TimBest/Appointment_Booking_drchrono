import datetime

from drchronoAPI.api import get_patients, get_doctors
from drchronoAPI.models import Patient, Doctor
from timezones.models import State
from utilities.functions import get_object_or_None


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
                    #'state': p['state'],
                    'state': get_object_or_None(State, state=p['state']),
                },
            )

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
