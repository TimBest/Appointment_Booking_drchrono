# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='practice',
            name='note',
            field=models.CharField(default=b'Booked online through http://localhost:8000/. Contact support@example.com for issues with your online booking.', max_length=255),
        ),
    ]
