from django import forms

from accounts.models import Patient, Practice


class SignupForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(),min_length=5)

    def __init__(self, *args, **kwargs):
        kwargs.pop('instance')
        super(SignupForm, self).__init__(*args, **kwargs)

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(),min_length=5)

class PatientForm(forms.ModelForm):
    def clean_first_name(self):
        return self.cleaned_data.get('first_name', '').strip()

    def clean_last_name(self):
        return self.cleaned_data.get('last_name', '').strip()

    def clean_email(self):
        return self.cleaned_data.get('email', '').strip()

    def clean_cell_phone(self):
        return self.cleaned_data.get('cell_phone', '').strip()

    class Meta:
        model = Patient
        fields = ('first_name', 'last_name', 'email', 'cell_phone', 'date_of_birth', 'gender')

class PracticeForm(forms.ModelForm):
    class Meta:
        model = Practice
        fields = ('note',)
