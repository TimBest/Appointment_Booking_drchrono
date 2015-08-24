from django.contrib.auth import logout as auth_logout
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.base import TemplateView

from accounts.forms import DoctorOrOfficeForm, PatientForm
from accounts.models import Practice
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
        for key, form in forms.iteritems():
            if self.request.user.is_authenticated() and hasattr(self.request.user, 'patient'):
                # save appointment via API
                form.save()
            else:
                pass
                # TODO redirect to signup
        return self.get_success_url()

appointment_form = AppointmentFormView.as_view()

class HomeView(TemplateView):
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['practices'] = Practice.objects.all()
        return context


home = HomeView.as_view()
