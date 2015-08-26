# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchronoAPI', '0004_appointmentprofiles'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointmentprofiles',
            name='doctor',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
