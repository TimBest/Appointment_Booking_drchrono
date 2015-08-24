from django import forms

from accounts.models import Patient


class PatientForm(forms.ModelForm):

    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'email', 'cell_phone', 'date_of_birth', 'gender')
