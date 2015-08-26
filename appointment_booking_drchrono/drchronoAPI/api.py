import datetime, requests, urllib

from drchronoAPI.models import Doctor, Office, Patient


class drchronoAPI(object):
    api_url = 'https://drchrono.com/api/'

    def __init__(self, practice):
        self.session = requests.Session()
        self.practice = practice
        social = practice.user.social_auth.get(user=practice.user)
        access_token = social.extra_data['access_token']
        self.session.headers.update({'Authorization': 'Bearer {0}'.format(access_token)})

    """ GET """
    def drchronoAPI_get(self, parameters, endnode):
        objects = []
        url = self.api_url + endnode + '?' + urllib.urlencode(parameters)
        while url:
            data = self.session.get(url).json()
            objects.extend(data['results'])
            url = data['next'] # A JSON null on the last page
        return objects

    def get_appointments(self, parameters={}):
        return self.drchronoAPI_get(parameters, 'appointments')

    def get_doctors(self, parameters={}):
        return self.drchronoAPI_get(parameters, 'doctors')

    def get_offices(self, parameters={}):
        return self.drchronoAPI_get(parameters, 'offices')

    def get_patients(self, parameters={}):
        return self.drchronoAPI_get(parameters, 'patients')

    """ PATCH """
    def activate_online_scheduling(self, office):
        data = {
            'online_scheduling': True,
        }
        url = self.api_url + 'offices/' + office.id

        self.session.patch(url, data=data)

        return None

    """ POST """
    def add_appointment(self, doctor, patient, office, scheduled_time, exam_room):
        data = {
            'doctor': int(doctor),
            'duration': 30, # in minutes
            'office': int(office),
            'exam_room': exam_room,
            'patient': patient,
            'scheduled_time': "%sT%s" % (scheduled_time.date(), scheduled_time.time()),
        }
        url = self.api_url + 'appointments'

        session = self.session.patch(url, data=data)
        assert session.status_code == 201 # HTTP 201 CREATED
        return None

    """ utils """
    def update_doctors_for_user(self, parameters={}):
        doctors = self.get_doctors(parameters)
        for d in doctors:
            doctor, created = Doctor.objects.update_or_create(
                id=d['id'],
                defaults= {
                    'user': self.practice.user,
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

    def update_offices_for_user(self, parameters = {}):
        offices = self.get_offices(parameters)
        for o in offices:
            office, created = Office.objects.update_or_create(
                id=o['id'],
                defaults= {
                    'user': self.practice.user,
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

    def update_patients_for_user(self, last_ran=None, parameters={}):
        if last_ran:
            parameters['since'] = last_ran
        patients = self.get_patients(parameters)
        for p in patients:
            date_of_birth = p['date_of_birth']
            if date_of_birth:
                year, month, day = [int(x) for x in p['date_of_birth'].split('-')]
                date_of_birth = datetime.date(year, month, day)
                patient, created = Patient.objects.update_or_create(
                    id=p['id'],
                    defaults= {
                        'user': self.practice.user,
                        'date_of_birth': date_of_birth,
                        'doctor': p['doctor'],
                        'first_name': p['first_name'],
                        'last_name': p['last_name'],
                        'cell_phone': p['cell_phone'],
                        'email': p['email'],
                        'state': p['state'],
                    },
                )
