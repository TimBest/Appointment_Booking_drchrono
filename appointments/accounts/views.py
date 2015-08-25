from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.base import TemplateView

import urllib

from accounts.forms import DoctorOrOfficeForm, PatientForm, SignupForm
from accounts.models import Practice
from drchronoAPI.api import add_appointment
from utilities.views import MultipleModelFormsView


# TODO: break this into 2 apps one for accounts and one for appointment info
def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect('/')

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

class SignupFormView(MultipleModelFormsView):
    form_classes = {
        'PatientForm' : PatientForm,
        'SignupForm' : SignupForm,
    }
    template_name='accounts/signup.html'
    success_url = 'home'

    def forms_valid(self, forms):
        signup_form = forms['SignupForm']
        patient = forms['PatientForm'].save(commit=False)

        password = signup_form.cleaned_data['password']
        user = User.objects.create_user(username=patient.email, email=patient.email,
                                        password=password)
        user = authenticate(username=patient.email, password=password)
        login(self.request, user)

        patient.user = user
        patient.id = 000
        patient.save()
        return self.get_success_url()

signup = SignupFormView.as_view()

class HomeView(TemplateView):
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['practices'] = Practice.objects.all()
        return context

home = HomeView.as_view()
