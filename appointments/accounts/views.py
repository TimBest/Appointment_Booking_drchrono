from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from utilities.views import MultipleModelFormsView
from greetings.forms import HappyBirthdayForm


def logout(request):
    """Logs out user"""
    auth_logout(request)
    return redirect('/')

class ProfileView(MultipleModelFormsView):
    form_classes = {'HappyBirthdayForm' : HappyBirthdayForm,}
    happybirthday_id=None
    template_name='accounts/profile.html'
    success_url = 'profile'

    def get_objects(self, queryset=None):
        from greetings.notifications import send_happy_birthdays
        send_happy_birthdays()
        return {'HappyBirthdayForm' : self.request.user.happy_birthday,}

profile = login_required(ProfileView.as_view())
