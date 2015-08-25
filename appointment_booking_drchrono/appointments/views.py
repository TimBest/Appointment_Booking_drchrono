from django.shortcuts import get_object_or_404, redirect

import urllib

from accounts.forms import PatientForm
from accounts.models import Practice
from appointments.forms import DoctorOrOfficeForm
from drchronoAPI.api import add_appointment
from utilities.views import MultipleModelFormsView


class AppointmentFormView(MultipleModelFormsView):
    form_classes = {
        'PatientForm' : PatientForm,
        'DoctorOrOfficeForm' : DoctorOrOfficeForm,
    }
    template_name='appointment_form.html'
    success_url = 'home'

    def dispatch(self, *args, **kwargs):
        practice_id = self.kwargs.get('practice_id', None)
        self.practice = get_object_or_404(Practice, user_id=practice_id)
        return super(AppointmentFormView, self).dispatch(*args, **kwargs)

    def get_objects(self, queryset=None):
        user = None
        if self.request.user.is_authenticated() and hasattr(self.request.user, 'patient'):
            user = self.request.user.patient
        return {
            'PatientForm' : user,
            'DoctorOrOfficeForm' : self.practice,
        }

    def forms_valid(self, forms):
        patient = forms['PatientForm']
        doctor_office = forms['DoctorOrOfficeForm']

        #add_appointment(self.practice, doctor, patient, office, scheduled_time)

        try:
            self.request.user.patient = patient
            self.request.user.patient.save()
        except:
            return "%s?%s" % ((redirect('signup')), urllib.urlencode(patient.cleaned_data))

        return self.get_success_url()

appointment_form = AppointmentFormView.as_view()
