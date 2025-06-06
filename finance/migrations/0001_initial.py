# Generated by Django 5.1.6 on 2025-05-29 13:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Account name e.g M-PESA', max_length=50)),
                ('paybill_number', models.CharField(help_text='Paybill number e.g 247247', max_length=100)),
                ('account_number', models.CharField(default='%(username)s', help_text='Any or combination of %(id)d, %(username)s,%(phone_number)s, %(email)s etc', max_length=100)),
                ('is_active', models.BooleanField(default=True, help_text='Account active status')),
                ('details', models.TextField(blank=True, help_text='Information related to this department.', null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The date and time when the account was created', verbose_name='Created At')),
            ],
            options={
                'verbose_name_plural': 'Account Details',
            },
        ),
        migrations.CreateModel(
            name='ExtraFee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Fee name', max_length=100)),
                ('details', models.TextField(help_text='What is this fee for?')),
                ('amount', models.DecimalField(decimal_places=2, help_text='Fee amount in Ksh', max_digits=8)),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated At')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, help_text='Transaction amount in Ksh', max_digits=10)),
                ('method', models.CharField(choices=[('CASH', 'Cash'), ('MPESA', 'm-pesa'), ('BANK', 'Bank'), ('OTHER', 'Other')], default='m-pesa', help_text='Select means of payment', max_length=20)),
                ('reference', models.CharField(help_text='Transaction ID or -- for cash.', max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The date and time when the order was created', verbose_name='Created At')),
            ],
        ),
        migrations.CreateModel(
            name='UserAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.DecimalField(decimal_places=2, default=0, help_text='Account balance', max_digits=8)),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='The date and time when the account was last updated', verbose_name='Updated At')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='The date and time when the aaccount was created', verbose_name='Created At')),
            ],
        ),
    ]
