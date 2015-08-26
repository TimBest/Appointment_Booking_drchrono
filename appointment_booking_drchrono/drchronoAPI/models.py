from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


class Doctor(models.Model):
    id = models.CharField(max_length=255, unique=True, primary_key=True,)
    user = models.ForeignKey(User, verbose_name=_('user'), related_name='doctors')
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    suffix = models.CharField(max_length=255, null=True)
    job_title = models.CharField(max_length=255, null=True)
    specialty = models.CharField(max_length=255, null=True)
    cell_phone = models.CharField(max_length=255, null=True)
    home_phone = models.CharField(max_length=255, null=True)
    office_phone = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    website = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    npi_number = models.CharField(max_length=255, null=True)
    group_npi_number = models.CharField(max_length=255, null=True)

    def __unicode__(self):
        return u'Dr %s %s' % (self.first_name, self.last_name)

class Office(models.Model):
    id = models.CharField(max_length=255, unique=True, primary_key=True,)
    user = models.ForeignKey(User, verbose_name=_('user'), related_name='offices')
    doctor = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    address = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    zip_code = models.CharField(max_length=255, null=True)
    phone_number = models.CharField(max_length=255, null=True)
    online_scheduling = models.CharField(max_length=255, null=True)
    online_timeslots = models.CharField(max_length=255, null=True)
    start_time = models.CharField(max_length=255, null=True)
    end_time = models.CharField(max_length=255, null=True)
    #exam_rooms = models.CharField(max_length=255, null=True)

    def __unicode__(self):
        return u'%s' % (self.name)

class Patient(models.Model):
    id = models.CharField(max_length=255, unique=True, primary_key=True,)
    user = models.ForeignKey(User, verbose_name=_('user'), related_name='patients')
    date_of_birth = models.DateField(null=True)
    doctor = models.CharField(max_length=255, null=True)
    first_name = models.CharField(max_length=255, null=True)
    last_name = models.CharField(max_length=255, null=True)
    cell_phone = models.CharField(max_length=255, null=True)
    email = models.EmailField(null=True)
    # TODO: Find out ho Washington DC is handled
    state = models.CharField(max_length=2, null=True)

    def __unicode__(self):
        return u'%s %s' % (self.first_name, self.last_name)

class AppointmentProfiles(models.Model):
    id = models.CharField(max_length=255, unique=True, primary_key=True,)
    user = models.ForeignKey(User, verbose_name=_('user'), related_name='appointment_profiles')
    color = models.CharField(max_length=255, null=True)
    duration = models.CharField(max_length=255, null=True)
    doctor = models.CharField(max_length=255, null=True)
    name = models.CharField(max_length=255, null=True)
    online_scheduling = models.NullBooleanField()
    reason = models.CharField(max_length=255, null=True)
    sort_order = models.CharField(max_length=255, null=True)


    def __unicode__(self):
        return u'%s' % (self.name)
