from django.db import models
from django.db.models import fields


# Create your models here.
class Patient(models.Model):
    Patient_name = models.CharField(max_length=60)
    age = models.PositiveSmallIntegerField()
    location = models.CharField(max_length=30)
    condition = models.CharField(max_length=150)
    medication = models.CharField(max_length=30)
    initial_visit = models.DateField()
    followup_appt = models.DateField()
    reminder_freq = models.PositiveSmallIntegerField()

class UserName(models.Model):
    username = models.CharField(max_length = 30)

class PassWord(models.Model):
    password = models.CharField(max_length = 30, unique=True)
