# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('drchronoAPI', '0005_appointmentprofiles_doctor'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExamRoom',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('index', models.CharField(max_length=255, null=True)),
                ('name', models.CharField(max_length=255, null=True)),
                ('online_scheduling', models.NullBooleanField()),
            ],
        ),
        migrations.AlterField(
            model_name='appointmentprofiles',
            name='user',
            field=models.ForeignKey(related_name='appointment_profiles', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='user',
            field=models.ForeignKey(related_name='doctors', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='office',
            name='user',
            field=models.ForeignKey(related_name='offices', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='patient',
            name='user',
            field=models.ForeignKey(related_name='patients', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='examroom',
            name='office',
            field=models.ForeignKey(related_name='exam_rooms', to='drchronoAPI.Office'),
        ),
        migrations.AddField(
            model_name='examroom',
            name='user',
            field=models.ForeignKey(related_name='all_exam_rooms', to=settings.AUTH_USER_MODEL),
        ),
    ]
