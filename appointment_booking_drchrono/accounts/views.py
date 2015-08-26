from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import FormView

from accounts.forms import PatientForm, PracticeForm, SignupForm, LoginForm
from accounts.models import Practice, Patient
from utilities.views import MultipleModelFormsView


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect(request.GET.get('next', '/'))

class SignupFormView(MultipleModelFormsView):
    form_classes = {
        'PatientForm' : PatientForm,
        'SignupForm' : SignupForm,
    }
    template_name='accounts/signup.html'
    success_url = 'home'

    def get_context_data(self, **kwargs):
        context = super(SignupFormView, self).get_context_data(**kwargs)
        context['id'] = self.request.GET.get('id',"/")
        return context

    def get_objects(self, queryset=None):
        try:
            patient = Patient()
            for key, value in self.request.GET.iteritems():
                setattr(patient, key, str(value))
        except:
            patient = None
        return {
            'PatientForm' : patient,
            'SignupForm' : None,
        }

    def forms_valid(self, forms):
        signup_form = forms['SignupForm']
        patient = forms['PatientForm'].save(commit=False)

        password = signup_form.cleaned_data['password']
        user = User.objects.create_user(username=patient.email, email=patient.email,
                                        password=password)
        user = authenticate(username=patient.email, password=password)
        auth_login(self.request, user)

        patient.user = user
        patient.id = self.request.POST.get('id', '')

        patient.save()
        return self.get_success_url()

signup = SignupFormView.as_view()

class LoginView(FormView):
    template_name = 'accounts/login.html'
    form_class = LoginForm

    def get_context_data(self, **kwargs):
        context = super(LoginView, self).get_context_data(**kwargs)
        form_class = self.get_form_class()
        context['login_form'] = self.get_form(form_class)
        context['next'] = self.request.GET.get('next',"/")
        return context

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data['email'],
                            password=form.cleaned_data['password'])
        auth_login(self.request, user)
        self.request.session.set_expiry(0)

        redirect_to = self.request.POST.get('next', '/')
        return HttpResponseRedirect(redirect_to)

login = LoginView.as_view()

class PracticeProfileView(MultipleModelFormsView):
    form_classes = {'PracticeForm' : PracticeForm,}
    template_name='accounts/practice_profile.html'
    success_url = 'practice_profile'

    def dispatch(self, *args, **kwargs):
        get_object_or_404(Practice, user=self.request.user)
        return super(PracticeProfileView, self).dispatch(*args, **kwargs)

    def get_objects(self, queryset=None):
        return {'PracticeForm' : self.request.user.practice,}

practice_profile = login_required(PracticeProfileView.as_view())

class PracticeProfileView(MultipleModelFormsView):
    form_classes = {'PatientForm' : PatientForm,}
    template_name='accounts/patient_profile.html'
    success_url = 'patient_profile'

    def dispatch(self, *args, **kwargs):
        get_object_or_404(Patient, user=self.request.user)
        return super(PracticeProfileView, self).dispatch(*args, **kwargs)

    def get_objects(self, queryset=None):
        return {'PatientForm' : self.request.user.patient,}

patient_profile = login_required(PracticeProfileView.as_view())
