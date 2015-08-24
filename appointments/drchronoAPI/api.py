import requests, urllib

API_URL = 'https://drchrono.com/api/'

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
