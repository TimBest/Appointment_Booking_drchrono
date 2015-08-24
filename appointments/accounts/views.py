from django.contrib.auth import logout as auth_logout
from django.shortcuts import redirect

from accounts.forms import PatientForm
from utilities.views import MultipleModelFormsView


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect('/')

class HomeView(MultipleModelFormsView):
    form_classes = {'PatientForm' : PatientForm,}
    happybirthday_id=None
    template_name='index.html'
    success_url = 'home'

    def get_objects(self, queryset=None):
        user = None
        if self.request.user.is_authenticated():
            user = self.request.user.patient
        return {'PatientForm' : user,}

    def forms_valid(self, forms):
        for key, form in forms.iteritems():
            if self.request.user.is_authenticated():
                form.save()
            else:
                pass
                # TODO redirect to signup
        return self.get_success_url()

home = HomeView.as_view()
