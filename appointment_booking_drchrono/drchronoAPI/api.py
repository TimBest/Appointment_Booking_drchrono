import datetime, requests, urllib

from drchronoAPI.models import AppointmentProfiles, Doctor, Office, Patient


class drchronoAPI(object):
    api_url = 'https://drchrono.com/api/'

    def __init__(self, practice):
        self.session = requests.Session()
        self.practice = practice
        social = practice.user.social_auth.get(user=practice.user)
        access_token = social.extra_data['access_token']
        self.session.headers.update({'Authorization': 'Bearer {0}'.format(access_token)})

    """ GET """
    def get(self, parameters, endnode):
        objects = []
        url = self.api_url + endnode + '?' + urllib.urlencode(parameters)
        while url:
            data = self.session.get(url).json()
            objects.extend(data['results'])
            url = data['next'] # A JSON null on the last page
        return objects

    def get_appointments(self, parameters={}):
        return self.get(parameters, 'appointments')

    def get_appointment_profiles(self, parameters={}):
        return self.get(parameters, 'appointment_profiles')

    def get_doctors(self, parameters={}):
        return self.get(parameters, 'doctors')

    def get_offices(self, parameters={}):
        return self.get(parameters, 'offices')

    def get_patients(self, parameters={}):
        return self.get(parameters, 'patients')

    """ PATCH """
    def activate_online_scheduling(self, office):
        data = {
            'online_scheduling': True,
        }
        url = self.api_url + 'offices/' + office.id

        self.session.patch(url, data=data)

        return None

    """ POST """
    def add_appointment(self, data={}):
        url = self.api_url + 'appointments'

        session = self.session.post(url, data=data)

        assert session.status_code == 201 # HTTP 201 CREATED
        return None

    """ utils """
    # TODO: these functions are almost identical. might be nice to have a generic update function
    def update_appointment_profiles(self, parameters={}):
        appointment_profiles = self.get_appointment_profiles(parameters)
        for profile in appointment_profiles:
            profile['user'] = self.practice.user
            profile, created = AppointmentProfiles.objects.update_or_create(
                id=profile['id'], defaults=profile,)

    def update_doctors_for_user(self, parameters={}):
        doctors = self.get_doctors(parameters)
        for doctor in doctors:
            doctor['user'] = self.practice.user
            doctor, created = Doctor.objects.update_or_create(
                id=doctor['id'], defaults=doctor)

    def update_offices_for_user(self, parameters = {}):
        offices = self.get_offices(parameters)
        for office in offices:
            office['user'] = self.practice.user
            office.pop('exam_rooms')
            # TODO: save exam rooms to seprate model
            office, created = Office.objects.update_or_create(
                id=office['id'], defaults=office)

    def update_patients_for_user(self, parameters={}):
        patients = self.get_patients(parameters)
        for patient in patients:
            patient['date_of_birth'] = datetime.date([int(x) for x in patient['date_of_birth'].split('-')])
            patient['user'] = self.practice.user
            patient, created = Patient.objects.update_or_create(
                id=patient['id'], defaults=patient,)
