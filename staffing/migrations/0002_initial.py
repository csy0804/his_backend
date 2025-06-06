# Generated by Django 5.1.6 on 2025-05-29 13:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('staffing', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='lead',
            field=models.OneToOneField(blank=True, help_text='Head of department', null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='doctor',
            name='user',
            field=models.OneToOneField(help_text='The user associated with this doctor', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='speciality',
            name='department',
            field=models.ForeignKey(help_text='Department name', on_delete=django.db.models.deletion.CASCADE, related_name='specialities', to='staffing.department'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='speciality',
            field=models.ForeignKey(blank=True, help_text="The doctor's speciality", null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctors', to='staffing.speciality'),
        ),
        migrations.AddField(
            model_name='doctor',
            name='working_days',
            field=models.ManyToManyField(help_text='Working days', related_name='doctors', to='staffing.workingday'),
        ),
    ]
