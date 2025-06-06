# Generated by Django 5.1.6 on 2025-05-29 13:38

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('external', '0002_initial'),
        ('finance', '0002_initial'),
        ('hospital', '0002_initial'),
        ('staffing', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='user',
            field=models.OneToOneField(help_text='The user associated with this patient', on_delete=django.db.models.deletion.CASCADE, related_name='patient', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='appointment',
            name='patient',
            field=models.ForeignKey(help_text='The patient for this appointment', on_delete=django.db.models.deletion.CASCADE, related_name='appointments', to='hospital.patient'),
        ),
        migrations.AddField(
            model_name='treatment',
            name='doctors',
            field=models.ManyToManyField(help_text='Doctors who administered treatment', related_name='treatments', to='staffing.doctor'),
        ),
        migrations.AddField(
            model_name='treatment',
            name='extra_fees',
            field=models.ManyToManyField(help_text='Extra treatment fees', related_name='treatments', to='finance.extrafee'),
        ),
        migrations.AddField(
            model_name='treatment',
            name='feedbacks',
            field=models.ManyToManyField(help_text='Treatment service feedback', related_name='treatments', to='external.servicefeedback'),
        ),
        migrations.AddField(
            model_name='treatment',
            name='patient',
            field=models.ForeignKey(help_text='The patient under treatment', on_delete=django.db.models.deletion.CASCADE, related_name='treatments', to='hospital.patient'),
        ),
        migrations.AddField(
            model_name='treatmentmedicine',
            name='medicine',
            field=models.ForeignKey(help_text='Medicine given', on_delete=django.db.models.deletion.RESTRICT, related_name='treament_medicine', to='hospital.medicine'),
        ),
        migrations.AddField(
            model_name='treatment',
            name='medicines',
            field=models.ManyToManyField(help_text='Treatment medicines', related_name='treatments', to='hospital.treatmentmedicine'),
        ),
    ]
