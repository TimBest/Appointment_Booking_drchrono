# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_patient_practice'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='doctor',
            field=models.CharField(default=75723, max_length=255),
            preserve_default=False,
        ),
    ]
