from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect

from accounts.forms import PatientForm
from drchronoAPI.api import get_doctors, get_offices
from utilities.views import MultipleModelFormsView


# TODO: break this into 2 apps one for accounts and one for appointment info
def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect('/')

class AppointmentFormView(MultipleModelFormsView):
    form_classes = {'PatientForm' : PatientForm,}
    template_name='index.html'
    success_url = 'home'

    def get_context_data(self, **kwargs):
        context = super(AppointmentFormView, self).get_context_data(**kwargs)
        context['doctors'] = get_doctors()
        context['offices'] = get_offices()

        return context

    def get_objects(self, queryset=None):
        user = None
        if self.request.user.is_authenticated():
            user = self.request.user.patient
        return {'PatientForm' : user,}

    def forms_valid(self, forms):
        for key, form in forms.iteritems():
            if self.request.user.is_authenticated():
                # save appointment via API
                form.save()
            else:
                pass
                # TODO redirect to signup
        return self.get_success_url()

appointment_form = AppointmentFormView.as_view()

class HomeView(MultipleModelFormsView):
    form_classes = {'PatientForm' : PatientForm,}
    template_name='index.html'
    success_url = 'home'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)

        return context

    def get_objects(self, queryset=None):
        user = None
        if self.request.user.is_authenticated():
            user = self.request.user.patient
        return {'PatientForm' : user,}

    def forms_valid(self, forms):
        for key, form in forms.iteritems():
            if self.request.user.is_authenticated():
                # save appointment via API
                form.save()
            else:
                pass
                # TODO redirect to signup
        return self.get_success_url()

home = HomeView.as_view()
