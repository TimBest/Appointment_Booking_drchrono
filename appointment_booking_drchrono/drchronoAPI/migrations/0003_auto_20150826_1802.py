# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchronoAPI', '0002_auto_20150826_1801'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='group_npi_number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='doctor',
            name='npi_number',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
