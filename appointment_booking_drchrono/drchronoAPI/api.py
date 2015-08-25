import requests, urllib


API_URL = 'https://drchrono.com/api/'
# TODO: rename user parameter to 'practice'
""" TODO: move this from function based to class based
    pass the class the user/practice and then we can use a session based requests
"""
""" GET """
def drchronoAPI_get(user, parameters, endnode):
    social = user.social_auth.get(user=user)
    access_token = social.extra_data['access_token']
    headers = {'Authorization': 'Bearer {0}'.format(access_token)}

    objects = []
    url = API_URL + endnode + '?' + urllib.urlencode(parameters)
    while url:
        data = requests.get(url, headers=headers).json()
        objects.extend(data['results'])
        url = data['next'] # A JSON null on the last page
    return objects

def get_appointments(user, parameters={}):
    return drchronoAPI_get(user, parameters, 'appointments')

def get_doctors(user, parameters={}):
    return drchronoAPI_get(user, parameters, 'doctors')

def get_offices(user, parameters={}):
    return drchronoAPI_get(user, parameters, 'offices')

def get_patients(user, parameters={}):
    return drchronoAPI_get(user, parameters, 'patients')

""" PATCH """
def activate_online_scheduling(user, office):
    social = user.social_auth.get(user=user)
    access_token = social.extra_data['access_token']
    headers = {'Authorization': 'Bearer {0}'.format(access_token)}

    data = {
        'online_scheduling': True,
    }
    url = API_URL + 'offices/' + office.id

    requests.patch(url, data=data, headers=headers)

    return None

""" POST """
def add_appointment(user, doctor, patient, office, scheduled_time):
    social = user.social_auth.get(user=user)
    access_token = social.extra_data['access_token']
    headers = {'Authorization': 'Bearer {0}'.format(access_token)}

    data = {
        'doctor': doctor,
        'duration': 30, # in minutes
        'office': office,
        'patient': patient,
        'scheduled_time': scheduled_time,
    }
    url = API_URL + 'appointments'

    r = requests.post(url, data=data, headers=headers)

    assert r.status_code == 201 # HTTP 201 CREATED
    return None
