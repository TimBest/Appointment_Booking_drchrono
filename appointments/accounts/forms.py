from django import forms

from accounts.models import Patient
from drchronoAPI.utils import update_doctors_for_user, update_offices_for_user


class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        # TODO add an autocomplete to gender field
        fields = ('first_name', 'last_name', 'email', 'cell_phone', 'date_of_birth', 'gender')

class DoctorOrOfficeForm(forms.Form):
    doctor = forms.ChoiceField(required=False)
    office = forms.ChoiceField(required=False)

    def __init__(self, *args, **kwargs):
        instance = kwargs.pop('instance')
        super(DoctorOrOfficeForm, self).__init__(*args, **kwargs)
        # TODO: schedule updates for all practices to run once a night
        update_doctors_for_user(user=instance.user)
        update_offices_for_user(user=instance.user)
        self.fields['doctor'].choices = [(d.id, str(d)) for d in instance.user.doctors.all()]
        self.fields['office'].choices= [(o.id, str(o)) for o in instance.user.offices.all()]
