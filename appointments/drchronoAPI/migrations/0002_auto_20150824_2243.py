# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drchronoAPI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='first_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='specialty',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='office',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='office',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='office',
            name='country',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='office',
            name='doctor',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='office',
            name='end_time',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='office',
            name='exam_rooms',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='office',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='office',
            name='online_scheduling',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='office',
            name='online_timeslots',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='office',
            name='phone_number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='office',
            name='start_time',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='office',
            name='state',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='office',
            name='zip_code',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='cell_phone',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='doctor',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='first_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='last_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='state',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
