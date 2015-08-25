from django import forms

from drchronoAPI.api import activate_online_scheduling
from drchronoAPI.utils import update_doctors_for_user, update_offices_for_user


class DoctorOrOfficeForm(forms.Form):
    # TODO: add a blank value
    doctor = forms.ChoiceField()
    office = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance')
        super(DoctorOrOfficeForm, self).__init__(*args, **kwargs)
        # TODO: schedule updates for all practices to run once a night
        update_doctors_for_user(user=instance.user)
        update_offices_for_user(user=instance.user)
        for office in instance.user.offices.all():
            activate_online_scheduling(user=instance.user, office=office)
        self.fields['doctor'].choices = [(d.id, d) for d in instance.user.doctors.all()]
        self.fields['office'].choices= [(o.id, o) for o in instance.user.offices.all()]

class ScheduleForm(forms.Form):
    # input format is set to the formate of the api
    appointment_date = forms.DateTimeField(input_formats=["%Y-%m-%dT%H:%M:%S"])

    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance')
        super(ScheduleForm, self).__init__(*args, **kwargs)
        # TODO: schedule updates for all practices to run once a night
        update_doctors_for_user(user=instance.user)
        self.fields['doctor'].choices = [(d.id, str(d)) for d in instance.user.doctors.all()]
