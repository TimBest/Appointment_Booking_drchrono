from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404

from collections import OrderedDict
import datetime
import urllib

from accounts.forms import PatientForm
from accounts.models import Practice
from appointments.forms import DoctorOrOfficeForm, ScheduleForm
from drchronoAPI.api import add_appointment, add_patient, get_appointments, get_patients
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
        # TODO: fix this entire mess
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
        patient_form = forms['PatientForm'].save(commit=False)
        doctor_office = forms['DoctorOrOfficeForm'].cleaned_data
        # remove ScheduleForm and just use time_slots from post
        schedule = forms['ScheduleForm'].cleaned_data

        doctor = doctor_office['doctor']
        office = doctor_office['office']

        # search for user
        patient = get_patients(self.practice.user, parameters={
            'date_of_birth':patient_form.date_of_birth,
            'first_name':patient_form.first_name,
            'last_name':patient_form.last_name,
            'gender':patient_form.gender,
        })

        if len(patient) == 0:
            add_patient(
                self.practice.user, doctor=doctor,
                date_of_birth=patient_form.date_of_birth,
                gender=patient_form.gender, data={
                    'first_name':patient_form.first_name,
                    'last_name':patient_form.last_name,
                    'cell_phone':patient_form.cell_phone,
                    'email':patient_form.email,
                })
            patient = get_patients(self.practice.user, parameters={
                'date_of_birth':patient_form.date_of_birth,
                'first_name':patient_form.first_name,
                'last_name':patient_form.last_name,
                'gender':patient_form.gender,
            })

        # TODO: handle multiple users in some way
        patient = patient[0]
        # Exam room set to 0 since I have not set up a model for saveing exam rooms
        add_appointment(self.practice.user, doctor, patient['id'], office, schedule['appointment_date'], exam_room=0)

        try:
            patient_form.id = patient['id']
            self.request.user.patient = patient_form
            self.request.user.patient.save()
        except:
            # TODO: pass uasers id with this
            return HttpResponseRedirect("%s?%s" % ((reverse('signup')), urllib.urlencode(patient)))

        return self.get_success_url()

appointment_form = AppointmentFormView.as_view()
