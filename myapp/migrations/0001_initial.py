# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-02-17 23:54
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ANC_Labs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ANC_Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_visit', models.DateField()),
                ('provider', models.CharField(max_length=60)),
                ('health_condition', models.CharField(max_length=60)),
                ('notes', models.TextField()),
                ('vitals', models.CharField(max_length=60)),
                ('medication', models.CharField(max_length=60)),
                ('labs', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='ANC_Vitals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.PositiveSmallIntegerField()),
                ('weight', models.PositiveSmallIntegerField()),
                ('sbp', models.PositiveSmallIntegerField()),
                ('dbp', models.PositiveSmallIntegerField()),
                ('heartrate', models.PositiveSmallIntegerField()),
                ('respiratory', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_appointment', models.DateField()),
                ('provider', models.CharField(max_length=60)),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Diagnosis_Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Imaging_Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='IWC_Labs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='IWC_Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_visit', models.DateField()),
                ('provider', models.CharField(max_length=60)),
                ('health_condition', models.CharField(max_length=60)),
                ('notes', models.TextField()),
                ('vitals', models.CharField(max_length=60)),
                ('medication', models.CharField(max_length=60)),
                ('labs', models.CharField(max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='IWC_Vitals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.PositiveSmallIntegerField()),
                ('weight', models.PositiveSmallIntegerField()),
                ('sbp', models.PositiveSmallIntegerField()),
                ('dbp', models.PositiveSmallIntegerField()),
                ('heartrate', models.PositiveSmallIntegerField()),
                ('respiratory', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Labs_Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Medications_Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patient_firstname', models.CharField(max_length=60)),
                ('Patient_lastname', models.CharField(max_length=60)),
                ('age', models.PositiveSmallIntegerField()),
                ('gender', models.CharField(max_length=60)),
                ('dob', models.DateField()),
                ('occupation', models.CharField(max_length=30)),
                ('contact_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('residence', models.CharField(max_length=60)),
                ('religion', models.CharField(max_length=60)),
                ('parent_guardian_name', models.CharField(max_length=60)),
                ('parent_guardian_contact_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('date_data_added', models.DateTimeField()),
                ('date_time_updated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient_ANC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patient_firstname', models.CharField(max_length=60)),
                ('Patient_lastname', models.CharField(max_length=60)),
                ('age', models.PositiveSmallIntegerField()),
                ('gender', models.CharField(max_length=60)),
                ('dob', models.DateField()),
                ('occupation', models.CharField(max_length=30)),
                ('contact_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('residence', models.CharField(max_length=60)),
                ('religion', models.CharField(max_length=60)),
                ('parent_guardian_name', models.CharField(max_length=60)),
                ('parent_guardian_contact_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('date_data_added', models.DateTimeField()),
                ('date_time_updated', models.DateTimeField()),
                ('parity', models.CharField(max_length=30)),
                ('lmp', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Patient_Diagnosis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diagnosis_condition', models.CharField(max_length=60)),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient_Imaging',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient_Inpatient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patient_firstname', models.CharField(max_length=60)),
                ('Patient_lastname', models.CharField(max_length=60)),
                ('age', models.PositiveSmallIntegerField()),
                ('gender', models.CharField(max_length=60)),
                ('dob', models.DateField()),
                ('occupation', models.CharField(max_length=30)),
                ('contact_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('residence', models.CharField(max_length=60)),
                ('religion', models.CharField(max_length=60)),
                ('parent_guardian_name', models.CharField(max_length=60)),
                ('parent_guardian_contact_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('date_data_added', models.DateTimeField()),
                ('date_time_updated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient_IWC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Patient_firstname', models.CharField(max_length=60)),
                ('Patient_lastname', models.CharField(max_length=60)),
                ('age', models.PositiveSmallIntegerField()),
                ('gender', models.CharField(max_length=60)),
                ('dob', models.DateField()),
                ('contact_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('residence', models.CharField(max_length=60)),
                ('parent_guardian_name', models.CharField(max_length=60)),
                ('parent_guardian_contact_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('date_data_added', models.DateTimeField()),
                ('date_time_updated', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient_Labs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=30)),
                ('notes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient_Medications',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(max_length=60)),
                ('prescription_start', models.DateField()),
                ('prescription_end', models.DateField()),
                ('prescribed_items', models.CharField(max_length=60)),
                ('prescription', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Patient_Vitals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.PositiveSmallIntegerField()),
                ('weight', models.PositiveSmallIntegerField()),
                ('sbp', models.PositiveSmallIntegerField()),
                ('dbp', models.PositiveSmallIntegerField()),
                ('heartrate', models.PositiveSmallIntegerField()),
                ('respiratory', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('doctor_name', models.CharField(max_length=60)),
                ('description', models.CharField(max_length=60)),
                ('date_data_added', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User_list',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_visit', models.DateField()),
                ('provider', models.CharField(max_length=60)),
                ('health_condition', models.CharField(max_length=60)),
                ('notes', models.TextField()),
                ('vitals', models.CharField(max_length=60)),
                ('medication', models.CharField(max_length=60)),
                ('labs', models.CharField(max_length=60)),
            ],
        ),
    ]