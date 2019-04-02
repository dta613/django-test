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
class patient(models.Model):
    patient_firstname = models.CharField(max_length=60)
    patient_lastname = models.CharField(max_length=60)
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
## FK many-to-one

class visit(models.Model):
    date_visit = models.DateField()
    provider = models.ForeignKey('provider', default=1, on_delete=models.CASCADE)
    health_condition = models.CharField(max_length=60)
    type = ('Please select type of appointment',
    'Consultation', 'Lab', 'Follow-up'
    )
    notes = models.TextField()
    vitals = models.CharField(max_length=60)
    medication = models.CharField(max_length=60)
    labs = models.CharField(max_length=60)
    patient_who_visited = models.ForeignKey('patient', default = 1, on_delete=models.CASCADE)
## FK many-to-one

class user_list(models.Model):
    username = models.CharField(max_length = 30)
    password = models.CharField(max_length = 30, unique=True)

class provider(models.Model):
    doctor_name = models.CharField(max_length=60)
    description = models.CharField(max_length=60)
    date_data_added = models.DateTimeField()

class patient_diagnosis(models.Model):
    diagnosis_condition = models.CharField(max_length=60)
    notes = models.TextField(blank=True)
    associated_visit = models.ForeignKey('visit', default=1, on_delete=models.CASCADE)

#How do we want to create this class object to retrieve values from a file? - Lookup List
class diagnosis_class(models.Model):
    diagnosis = models.ForeignKey('patient_diagnosis', default=1, on_delete=models.CASCADE)
    diagnosis_name = models.CharField(max_length=60, blank=True)
    description = models.TextField(blank=True)

class appointment(models.Model):
    date_appointment = models.DateField()
    provider = models.ForeignKey('provider', default=1, on_delete=models.CASCADE)
    type = ('Please select type of appointment',
    'Consultation', 'Lab', 'Follow-up'
    )
    status = ('Please select type of status',
    'Scheduled', 'Canceled', 'Missed'
    )
    notes = models.TextField()
    associated_visit  = models.ForeignKey('patient', default=1, on_delete=models.CASCADE)


class patient_vitals(models.Model):
    temperature = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    sbp = models.PositiveSmallIntegerField()
    dbp = models.PositiveSmallIntegerField()
    heartrate = models.PositiveSmallIntegerField()
    respiratory = models.PositiveSmallIntegerField()
    associated_visit  = models.ForeignKey('visit', default=1, on_delete=models.CASCADE)


class patient_medications(models.Model):
    provider = models.CharField(max_length=60)
    prescription_start = models.DateField()
    prescription_end = models.DateField()
    prescribed_items = models.CharField(max_length=60)
    prescription = models.TextField()
    associated_visit  = models.ForeignKey('visit', default=1, on_delete=models.CASCADE)
    medications = models.ForeignKey('medications_class', default=1, on_delete=models.CASCADE)
    notes = models.TextField(blank=True)

#How do we want to create this class to retrieve values from a file? - LookupList

class medications_class(models.Model):
    medication_name = models.CharField(max_length=60,blank=True)
    medications = models.ForeignKey('patient_medications', default=1, on_delete=models.CASCADE)

class patient_labs(models.Model):
    type = models.CharField(max_length=30)
    notes = models.TextField(blank=True)
    associated_visit  = models.ForeignKey('visit', default=1, on_delete=models.CASCADE)

#What are the names of the labs that needs to be in this class object?
#How do we configure for dynamic user entry to add to the choices?
class labs_class(models.Model):
    labs = models.ForeignKey('patient_labs', default=1, on_delete=models.CASCADE)
    labs_name = models.CharField(max_length=60, blank=True)
    description = models.TextField(blank=True)

class patient_imaging(models.Model):
    type = models.CharField(max_length=30)
    notes = models.TextField()
    associated_visit  = models.ForeignKey('visit', default=1, on_delete=models.CASCADE)

#How do we configure for dynamic user entry to add to the choices?
class imaging_class(models.Model):
    imaging = models.ForeignKey('patient_imaging', default=1, on_delete=models.CASCADE)
    imaging_name = models.CharField(max_length=60, blank=True)
    description = models.TextField(blank=True)

## Patient for Ante-natal care, supporting pregnant women (paturient)
class patient_anc(models.Model):
    patient_firstname = models.CharField(max_length=60)
    patient_lastname = models.CharField(max_length=60)
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

## Patient for infant wellness care, supporting women and infants
class patient_iwc(models.Model):
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

## Patient that gets admitted to the hospital
class patient_inpatient(models.Model):
    patient_firstname = models.CharField(max_length=60)
    patient_lastname = models.CharField(max_length=60)
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

class anc_visit(models.Model):
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
    anc_patient = models.ForeignKey('patient_anc', default=1, on_delete=models.CASCADE)

class iwc_visit(models.Model):
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
    iwc_patient = models.ForeignKey('patient_iwc', default=1, on_delete=models.CASCADE)


class anc_vitals(models.Model):
    temperature = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    sbp = models.PositiveSmallIntegerField()
    dbp = models.PositiveSmallIntegerField()
    heartrate = models.PositiveSmallIntegerField()
    respiratory = models.PositiveSmallIntegerField()
    associated_visit = models.ForeignKey('anc_visit', default=1, on_delete=models.CASCADE)


class iwc_vitals(models.Model):
    temperature = models.PositiveSmallIntegerField()
    weight = models.PositiveSmallIntegerField()
    sbp = models.PositiveSmallIntegerField()
    dbp = models.PositiveSmallIntegerField()
    heartrate = models.PositiveSmallIntegerField()
    respiratory = models.PositiveSmallIntegerField()
    associated_visit = models.ForeignKey('iwc_visit', default=1, on_delete=models.CASCADE)


class anc_labs(models.Model):
    type = models.CharField(max_length=30)
    notes = models.TextField()
    associated_visit = models.ForeignKey('anc_visit', default=1, on_delete=models.CASCADE)


class iwc_labs(models.Model):
    type = models.CharField(max_length=30)
    notes = models.TextField()
    associated_visit = models.ForeignKey('iwc_visit', default=1, on_delete=models.CASCADE)


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
