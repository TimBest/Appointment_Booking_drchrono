from django import forms

from accounts.models import Patient


class SignupForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(),min_length=5)

    def __init__(self, *args, **kwargs):
        kwargs.pop('instance')
        super(SignupForm, self).__init__(*args, **kwargs)

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput(),min_length=5)

class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        # TODO add an autocomplete to gender field or add select choice widget
        """widgets = {
          'gender' : forms.select(choices=('Male', 'Female', 'Other')),
        }"""
        fields = ('first_name', 'last_name', 'email', 'cell_phone', 'date_of_birth', 'gender')
