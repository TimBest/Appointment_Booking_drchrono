from django.contrib.gis.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _


GENDER_CHOICES = (
    ('f', _('Female')),
    ('m', _('Male')),
    ('o', _('Other')),
)

class Practice(models.Model):
    user = models.OneToOneField(User, unique=True, primary_key=True)

class Patient(models.Model):
    user = models.OneToOneField(User, unique=True, primary_key=True)
    id = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    cell_phone = models.CharField(max_length=255)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,
                              default=GENDER_CHOICES[0][0])
    email = models.EmailField()
