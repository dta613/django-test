# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import fields
# from phonenumber_field.modelfields import PhoneNumberField

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

# Foreign key constraints built on:
class Patient(models.Model):
    patientid = models.PositiveSmallIntegerField()
    Patient_firstname = models.CharField(max_length=60)
    Patient_lastname = models.CharField(max_length=60)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=60)
    # dob = models.DateField() <- calculate age based on dob
    occupation = models.CharField(max_length=30)
    # contact_number = PhoneNumberField()
    residence = models.CharField(max_length=60)
    religion = models.CharField(max_length=60)
    parent_guardian_name = models.CharField(max_length=60)
    # parent_guardian_contact_number = PhoneNumberField()
    # date_data_added = models.DateTimeField()
    date_time_updated = models.DateTimeField()


class User_list(models.Model):
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30, unique=True)

class Provider(models.Model):
    doctor_name = models.CharField(max_length=60)
    description = models.CharField(max_length=60)
    date_data_added = models.DateTimeField()

class Patient_Diagnosis(models.Model):
    diagnosis_condition = models.CharField(max_length=60)
    notes = models.TextField()

#How do we want to create this class object to retrieve values from a file? - Lookup List
class Diagnosis_Class(models.Model):
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

class Appointment(models.Model):
    date_appointment = models.DateField()
    provider = models.CharField(max_length=60)
    type = ('Please select type of appointment',
    'Consultation', 'Lab', 'Follow-up'
    )
    status = ('Please select type of status',
    'Scheduled', 'Canceled', 'Missed'
    )
    notes = models.TextField()


class Patient_Vitals(models.Model):
    temperature = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    sbp = models.PositiveSmallIntegerField()
    dbp = models.PositiveSmallIntegerField()
    heartrate = models.PositiveSmallIntegerField()
    respiratory = models.PositiveSmallIntegerField()

class Patient_Medications(models.Model):
    provider = models.CharField(max_length=60)
    prescription_start = models.DateField()
    prescription_end = models.DateField()
    prescribed_items = models.CharField(max_length=60)
    prescription = models.TextField()

#How do we want to create this class to retrieve values from a file? - LookupList

class Medications_Class(models.Model):
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

class Patient_Labs(models.Model):
    type = models.CharField(max_length=30)
    notes = models.TextField()

#What are the names of the labs that needs to be in this class object?
#How do we configure for dynamic user entry to add to the choices?
class Labs_Class(models.Model):
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


class Patient_Imaging(models.Model):
    type = models.CharField(max_length=30)
    notes = models.TextField()

#How do we configure for dynamic user entry to add to the choices?
class Imaging_Class(models.Model):
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


class Visit(models.Model):
    date_visit = models.DateField()
    provider = models.CharField(max_length=60)
    health_condition = models.CharField(max_length=60)
    type = ('Please select type of appointment',
    'Consultation', 'Lab', 'Follow-up'
    )
    notes = models.TextField()
    vitals = models.CharField(max_length=60)
    medication = models.CharField(max_length=60)
    labs = models.CharField(max_length=60)
    patient_who_visited = models.ForeignKey('Patient.patientid = 1',  on_delete=models.CASCADE)


class Patient_ANC(models.Model):
    Patient_firstname = models.CharField(max_length=60)
    Patient_lastname = models.CharField(max_length=60)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=60)
    dob = models.DateField()
    occupation = models.CharField(max_length=30)
    # contact_number = PhoneNumberField()
    residence = models.CharField(max_length=60)
    religion = models.CharField(max_length=60)
    parent_guardian_name = models.CharField(max_length=60)
    # parent_guardian_contact_number = PhoneNumberField()
    date_data_added = models.DateTimeField()
    date_time_updated = models.DateTimeField()
    parity = models.CharField(max_length=30)
    lmp = models.CharField(max_length=30)


class Patient_IWC(models.Model):
    Patient_firstname = models.CharField(max_length=60)
    Patient_lastname = models.CharField(max_length=60)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=60)
    dob = models.DateField()
    # contact_number = PhoneNumberField()
    residence = models.CharField(max_length=60)
    parent_guardian_name = models.CharField(max_length=60)
    # parent_guardian_contact_number = PhoneNumberField()
    date_data_added = models.DateTimeField()
    date_time_updated = models.DateTimeField()


class Patient_Inpatient(models.Model):
    Patient_firstname = models.CharField(max_length=60)
    Patient_lastname = models.CharField(max_length=60)
    age = models.PositiveSmallIntegerField()
    gender = models.CharField(max_length=60)
    dob = models.DateField()
    occupation = models.CharField(max_length=30)
    # contact_number = PhoneNumberField()
    residence = models.CharField(max_length=60)
    religion = models.CharField(max_length=60)
    parent_guardian_name = models.CharField(max_length=60)
    # parent_guardian_contact_number = PhoneNumberField()
    date_data_added = models.DateTimeField()
    date_time_updated = models.DateTimeField()

class ANC_Vitals(models.Model):
    temperature = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    sbp = models.PositiveSmallIntegerField()
    dbp = models.PositiveSmallIntegerField()
    heartrate = models.PositiveSmallIntegerField()
    respiratory = models.PositiveSmallIntegerField()

class IWC_Vitals(models.Model):
    temperature = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    sbp = models.PositiveSmallIntegerField()
    dbp = models.PositiveSmallIntegerField()
    heartrate = models.PositiveSmallIntegerField()
    respiratory = models.PositiveSmallIntegerField()

class ANC_Labs(models.Model):
    type = models.CharField(max_length=30)
    notes = models.TextField()

class IWC_Labs(models.Model):
    type = models.CharField(max_length=30)
    notes = models.TextField()

class ANC_Visit(models.Model):
    date_visit = models.DateField()
    provider = models.CharField(max_length=60)
    health_condition = models.CharField(max_length=60)
    type = ('Please select type of appointment',
    'Consultation', 'Lab', 'Follow-up'
    )
    notes = models.TextField()
    vitals = models.CharField(max_length=60)
    medication = models.CharField(max_length=60)
    labs = models.CharField(max_length=60)

class IWC_Visit(models.Model):
    date_visit = models.DateField()
    provider = models.CharField(max_length=60)
    health_condition = models.CharField(max_length=60)
    type = ('Please select type of appointment',
    'Consultation', 'Lab', 'Follow-up'
    )
    notes = models.TextField()
    vitals = models.CharField(max_length=60)
    medication = models.CharField(max_length=60)
    labs = models.CharField(max_length=60)

#     text, date, bytea
# smallint, text, char(n) or text for pass


# account:
# a_id,username, salt, passhash

# staff:
# staffid, username(link), email, fname, lname, address, etc

# doctor:
# doctor_id, name, gender, specialty, dob,

# patient:
# patientid, fname, lname, dob, gender, phone1, phone2, email, address, religion, occupation, parent_guardian_name,

# patient_appointments:
# id, date, type, status, notes, patientid(link),

# patient_visit:
# visitid, date, type, status, location, action, reason, patientid(link),vitalsid(link), medicationid(link), labs(link), imaging(link), Diagnosisid(link), doctor(link)

# patient_vitals:
# id, recorddate, temp, weight, height, sbp, dbp, heartrate, resprate, visitid(link)

# patient_medication:
# id, prescdate, penddate, visit, med1, med2, notes, visitid(link)

# patient_labs:
# id, visit, type, notes, visitid(link)

# patient_imaging:
# id, visit, type, notes, visitid(link)

# Diagnosis:
# diagnosis_id, diagnosis_classid(link), visitid(link), date, actual_description, etc

# diagnosisClass:
# diagnosis_classid, name, description, etc
