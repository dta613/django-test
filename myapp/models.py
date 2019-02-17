# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import fields
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.



# Notes and Resources:
#https://djangobook.com/mdj2-models/
# https://opal.openhealthcare.org.uk/docs/guides/topic-guides/
# What are the tables that need to be linked?
# Patient to Provider
# Patient to Visit
# Patient to Appointment
# Patient_Diagnosis to Diagnosis_Class
# Patient_Diagnosis to Patient
# Visit to Patient_Imaging
# Visit to Patient_Labs
# Visit to Patient_Vitals
# Visit to Patient_Medications
# Patient_Labs to Labs_Class
# Patient_Vitals to Vitals_Class
# Patient_Imaging to Imaging_Class
# Patient_Medications to Medications_Class
# Patient_Medications to Patient_ANC
# Patient_Medications to Patient_IWC
# Patient_Imaging to ANC_Visit
# Patient_Imaging to IWC_Visit
# Patient_Diagnosis to ANC_Visit
# Patient_Diagnosis to IWC_Visit
# Patient_Labs to ANC_Visit
# Patient_Labs to IWC_Visit
# ANC_Visit to Patient_ANC
# IWC_Visit to Patient_IWC
# Patient_Diagnosis to Patient_IWC
# Patient_Diagnosis to Patient_ANC
# Appointment to Patient_ANC
# Appointment to Patient_IWC


class Patient(models.Model):
    Patient_firstname = models.CharField(max_length=60)
    Patient_lastname = models.CharField(max_length=60)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=60)
    dob = models.DateField()
    occupation = models.CharField(max_length=30)
    contact_number = models.PhoneNumberField()
    residence = models.CharField(max_length=60)
    religion = models.CharField(max_length=60)
    parent_guardian_name = models.CharField(max_length=60)
    parent_guardian_contact_number = models.PhoneNumberField()
    date_data_added = models.DateTimeField()
    date_time_updated = models.DateTimeField()

class User_list(models.Model):
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30, unique=True)

class Provider(models.Models):
    doctor_name = models.CharField(max_length=60)
    description = models.CharField(max_length=60)
    date_data_added = models.DateTimeField()

class Patient_Diagnosis(models.Models):
    diagnosis_condition = models.CharField(max_length=60)
    notes = models.TextField()

#How do we want to create this class object to retrieve values from a file? - Lookup List
class Diagnosis_Class(models.Models):
    diagnosis_option_value = (
        ('', 'Please select a diagnosis'),
        ('simple malaria', 'severe malaria'),
        ('a-thalassaemia syndromes', 'a-thalassaemia syndromes'),
        ('Sickle cell syndromes', 'Sickle cell syndromes'),
        ('Other haemoglobin variants','Other haemoglobin variants'),
        ('Rare cell membrane disorders','Rare cell membrane disorders'),
        ('Rare cell enzyme disorders','Rare cell enzyme disorders'),
        ('Congenital dyserythropoietic anaemias','Congenital dyserythropoietic anaemias')
    )

class Appointment(models.Models):
    date_appointment = models.DateField()
    provider = Provider.doctor_name()
    type = ('Please select type of appointment',
    'Consultation', 'Lab', 'Follow-up'
    )
    status = ('Please select type of status',
    'Scheduled', 'Canceled', 'Missed'
    )
    notes = models.TextField()

class Patient_Vitals
    temperature = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    sbp = models.PositiveSmallIntegerField()
    dbp = models.PositiveSmallIntegerField()
    heartrate = models.PositiveSmallIntegerField()
    respiratory = models.PositiveSmallIntegerField()

class Patient_Medications
    provider = Provider.doctor_name()
    prescription_start = models.DateField()
    prescription_end = models.DateField()
    prescribed_items = models.ChoiceField()
    prescription = models.TextField()

#How do we want to create this class to retrieve values from a file? - LookupList

class Medications_Class
    medication_option_value = (
        ('', 'Please select a medication'),
        ('simple malaria', 'severe malaria'),
        ('a-thalassaemia syndromes', 'a-thalassaemia syndromes'),
        ('Sickle cell syndromes', 'Sickle cell syndromes'),
        ('Other haemoglobin variants','Other haemoglobin variants'),
        ('Rare cell membrane disorders','Rare cell membrane disorders'),
        ('Rare cell enzyme disorders','Rare cell enzyme disorders'),
        ('Congenital dyserythropoietic anaemias','Congenital dyserythropoietic anaemias')
    )

class Patient_Labs
    type = models.CharField(max_length=30)
    notes = models.TextField()

#What are the names of the labs that needs to be in this class object?
#How do we configure for dynamic user entry to add to the choices?
class Labs_Class
    labs_option_value = (
        ('', 'Please select a lab type'),
        ('simple malaria', 'severe malaria'),
        ('a-thalassaemia syndromes', 'a-thalassaemia syndromes'),
        ('Sickle cell syndromes', 'Sickle cell syndromes'),
        ('Other haemoglobin variants','Other haemoglobin variants'),
        ('Rare cell membrane disorders','Rare cell membrane disorders'),
        ('Rare cell enzyme disorders','Rare cell enzyme disorders'),
        ('Congenital dyserythropoietic anaemias','Congenital dyserythropoietic anaemias')
    )


class Patient_Imaging
    type = models.CharField(max_length=30)
    notes = models.TextField()

#How do we configure for dynamic user entry to add to the choices?
class Imaging_Class
    imaging_option_value = (
        ('', 'Please select a imaging type'),
        ('simple malaria', 'severe malaria'),
        ('a-thalassaemia syndromes', 'a-thalassaemia syndromes'),
        ('Sickle cell syndromes', 'Sickle cell syndromes'),
        ('Other haemoglobin variants','Other haemoglobin variants'),
        ('Rare cell membrane disorders','Rare cell membrane disorders'),
        ('Rare cell enzyme disorders','Rare cell enzyme disorders'),
        ('Congenital dyserythropoietic anaemias','Congenital dyserythropoietic anaemias')
    )


class Visit(models.Models):
    date_visit = models.DateField()
    provider = Provider.doctor_name()
    health_condition = Patient_Diagnosis.diagnosis_condition()
    type = ('Please select type of appointment',
    'Consultation', 'Lab', 'Follow-up'
    )
    notes = models.TextField()
    vitals = Vitals_Class()
    medication = Patient_Medications()
    labs = Patient_Labs()

class Patient_ANC
    Patient_firstname = models.CharField(max_length=60)
    Patient_lastname = models.CharField(max_length=60)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=60)
    dob = models.DateField()
    occupation = models.CharField(max_length=30)
    contact_number = models.PhoneNumberField()
    residence = models.CharField(max_length=60)
    religion = models.CharField(max_length=60)
    parent_guardian_name = models.CharField(max_length=60)
    parent_guardian_contact_number = models.PhoneNumberField()
    date_data_added = models.DateTimeField()
    date_time_updated = models.DateTimeField()
    parity = models.CharField(max_length=30)
    lmp = models.CharField(max_length=30)


class Patient_IWC
    Patient_firstname = models.CharField(max_length=60)
    Patient_lastname = models.CharField(max_length=60)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=60)
    dob = models.DateField()
    contact_number = models.PhoneNumberField()
    residence = models.CharField(max_length=60)
    parent_guardian_name = models.CharField(max_length=60)
    parent_guardian_contact_number = models.PhoneNumberField()
    date_data_added = models.DateTimeField()
    date_time_updated = models.DateTimeField()


class Patient_Inpatient
    Patient_firstname = models.CharField(max_length=60)
    Patient_lastname = models.CharField(max_length=60)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=60)
    dob = models.DateField()
    occupation = models.CharField(max_length=30)
    contact_number = models.PhoneNumberField()
    residence = models.CharField(max_length=60)
    religion = models.CharField(max_length=60)
    parent_guardian_name = models.CharField(max_length=60)
    parent_guardian_contact_number = models.PhoneNumberField()
    date_data_added = models.DateTimeField()
    date_time_updated = models.DateTimeField()

class ANC_Vitals
    temperature = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    sbp = models.PositiveSmallIntegerField()
    dbp = models.PositiveSmallIntegerField()
    heartrate = models.PositiveSmallIntegerField()
    respiratory = models.PositiveSmallIntegerField()

class IWC_Vitals
    temperature = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    sbp = models.PositiveSmallIntegerField()
    dbp = models.PositiveSmallIntegerField()
    heartrate = models.PositiveSmallIntegerField()
    respiratory = models.PositiveSmallIntegerField()

class ANC_Labs
    type = models.CharField(max_length=30)
    notes = models.TextField()

class IWC_Labs
    type = models.CharField(max_length=30)
    notes = models.TextField()

class ANC_Visit
    date_visit = models.DateField()
    provider = Provider.doctor_name()
    health_condition = Patient_Diagnosis.diagnosis_condition()
    type = ('Please select type of appointment',
    'Consultation', 'Lab', 'Follow-up'
    )
    notes = models.TextField()
    vitals = Vitals_Class()
    medication = Patient_Medications()
    labs = Patient_Labs()

class IWC_Visit
    date_visit = models.DateField()
    provider = Provider.doctor_name()
    health_condition = Patient_Diagnosis.diagnosis_condition()
    type = ('Please select type of appointment',
    'Consultation', 'Lab', 'Follow-up'
    )
    notes = models.TextField()
    vitals = Vitals_Class()
    medication = Patient_Medications()
    labs = Patient_Labs()