from django.contrib.gis.db import models
from django.contrib.auth.models import User
#from django.utils.translation import ugettext as _


class Practice(models.Model):
    user = models.OneToOneField(User, unique=True, primary_key=True)

class Patient(models.Model):
    user = models.OneToOneField(User, unique=True, primary_key=True)
    id = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    cell_phone = models.CharField(max_length=255)
    email = models.EmailField()
