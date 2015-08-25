from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from collections import OrderedDict
import datetime
import urllib

from accounts.forms import PatientForm
from accounts.models import Practice
from appointments.forms import DoctorOrOfficeForm, ScheduleForm
from drchronoAPI.api import add_appointment, get_appointments
from utilities.views import MultipleModelFormsView


class AppointmentFormView(MultipleModelFormsView):
    form_classes = {
        'DoctorOrOfficeForm' : DoctorOrOfficeForm,
        'PatientForm' : PatientForm,
        'ScheduleForm' : ScheduleForm,
    }
    template_name='appointment_form.html'
    success_url = 'home'

    def dispatch(self, *args, **kwargs):
        practice_id = self.kwargs.get('practice_id', None)
        self.practice = get_object_or_404(Practice, user_id=practice_id)
        return super(AppointmentFormView, self).dispatch(*args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(AppointmentFormView, self).get_context_data(**kwargs)
        number_of_days = 7
        today = datetime.date(year=2015, month=8, day=11) #datetime.date.today()
        end = today + datetime.timedelta(days=number_of_days)

        # TODO: this does not need to be created each time
        start = datetime.datetime(year=2015,month=1,day=1,hour=9)
        time_slots = []
        for half_hour in range(0, 480, 30):
            time_slots.append((start + datetime.timedelta(minutes=half_hour)).time())

        available_appointments = OrderedDict()
        for days in range(7):
            date = today + datetime.timedelta(days=days)
            available_appointments[date] = list(time_slots)

        #appointments = get_appointments(self.practice.user, {'date_range': "%s/%s" % (today, end)})
        appointments = get_appointments(self.practice.user, {'date_range':'2015-08-11/2015-08-18'})

        for appointment in appointments:
            scheduled_time = datetime.datetime.strptime(appointment['scheduled_time'], '%Y-%m-%dT%H:%M:%S')
            # round to the nearest half hour

            scheduled_time -= datetime.timedelta(minutes=scheduled_time.minute % 30)

            duration = appointment['duration']
            available_appointments[scheduled_time.date()].remove((scheduled_time).time())

            for half_hour in range(0, duration, 30):
                try:
                    available_appointments[scheduled_time.date()].remove((scheduled_time + datetime.timedelta(minutes=half_hour)).time())
                except:
                    pass
                    # print scheduled_time.date()
                    # print (scheduled_time + datetime.timedelta(minutes=half_hour)).time()
                    # print available_appointments[scheduled_time.date()]"""
        context['available_appointments'] = available_appointments
        return context

    def get_objects(self, queryset=None):
        user = None
        if self.request.user.is_authenticated() and hasattr(self.request.user, 'patient'):
            user = self.request.user.patient
        return {
            'DoctorOrOfficeForm' : self.practice,
            'PatientForm' : user,
            'ScheduleForm' : None,
        }

    def forms_valid(self, forms):
        patient = forms['PatientForm']
        doctor_office = forms['DoctorOrOfficeForm']

        #add_appointment(self.practice, doctor, patient, office, scheduled_time)

        try:
            self.request.user.patient = patient
            self.request.user.patient.save()
        except:
            return HttpResponseRedirect("%s?%s" % ((reverse('signup')), urllib.urlencode(patient.cleaned_data)))

        return self.get_success_url()

appointment_form = AppointmentFormView.as_view()
