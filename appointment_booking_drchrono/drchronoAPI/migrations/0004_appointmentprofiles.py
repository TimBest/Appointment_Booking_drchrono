# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drchronoAPI', '0003_auto_20150826_1802'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppointmentProfiles',
            fields=[
                ('id', models.CharField(max_length=255, unique=True, serialize=False, primary_key=True)),
                ('color', models.CharField(max_length=255, null=True)),
                ('duration', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('online_scheduling', models.NullBooleanField()),
                ('reason', models.CharField(max_length=255, null=True)),
                ('sort_order', models.CharField(max_length=255, null=True)),
                ('user', models.ForeignKey(related_name='appointment_profiles', verbose_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
