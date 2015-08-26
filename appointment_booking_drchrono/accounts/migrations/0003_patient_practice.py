# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_practice_note'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='practice',
            field=models.ForeignKey(related_name='online_appointment_patients', default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
