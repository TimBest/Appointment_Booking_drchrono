from django import forms
from django.utils.translation import ugettext as _

from drchronoAPI.api import drchronoAPI


class AppointmentInfoForm(forms.Form):
    # TODO: add a 'any'' value
    doctor = forms.ChoiceField()
    office = forms.ChoiceField()
    profile = forms.ChoiceField(label=_("Appointment Type"))

    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance')
        super(AppointmentInfoForm, self).__init__(*args, **kwargs)
        # TODO: schedule updates for all practices to run once a night
        drchrono = drchronoAPI(instance.user.practice)
        drchrono.update_doctors_for_user()
        drchrono.update_offices_for_user()
        drchrono.update_appointment_profiles()
        for office in instance.user.offices.all():
            drchrono.activate_online_scheduling(office=office)
        self.fields['profile'].choices = [(p.id, p) for p in instance.user.appointment_profiles.all()]
        self.fields['doctor'].choices = [(d.id, d) for d in instance.user.doctors.all()]
        self.fields['office'].choices= [(o.id, o) for o in instance.user.offices.all()]

class ScheduleForm(forms.Form):
    # input format is set to the formate of the api
    appointment_date = forms.DateTimeField(input_formats=["%Y-%m-%dT%H:%M:%S"])

    def __init__(self, *args, **kwargs):
        kwargs.pop('instance')
        super(ScheduleForm, self).__init__(*args, **kwargs)
