from django import forms

from drchronoAPI.api import drchronoAPI


class DoctorOrOfficeForm(forms.Form):
    # TODO: add a blank value
    doctor = forms.ChoiceField()
    office = forms.ChoiceField()

    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance')
        super(DoctorOrOfficeForm, self).__init__(*args, **kwargs)
        # TODO: schedule updates for all practices to run once a night
        drchrono = drchronoAPI(instance.user.practice)
        drchrono.update_doctors_for_user()
        drchrono.update_offices_for_user()
        for office in instance.user.offices.all():
            drchrono.activate_online_scheduling(office=office)
        self.fields['doctor'].choices = [(d.id, d) for d in instance.user.doctors.all()]
        self.fields['office'].choices= [(o.id, o) for o in instance.user.offices.all()]

class ScheduleForm(forms.Form):
    # input format is set to the formate of the api
    appointment_date = forms.DateTimeField(input_formats=["%Y-%m-%dT%H:%M:%S"])

    def __init__(self, *args, **kwargs):
        kwargs.pop('instance')
        super(ScheduleForm, self).__init__(*args, **kwargs)
