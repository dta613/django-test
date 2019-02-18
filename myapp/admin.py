# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from myapp.models import Patient
#Register your models here.

class Patient_admin(admin.ModelAdmin):
    list_display = ('Patient_firstname', 'Patient_lastname', 'age', 'gender',
    'dob', 'occupation', 'contact_number', 'residence','religion', 'parent_guardian_name',
    'parent_guardian_contact_number', 'date_data_added', 'date_time_updated')
    pass

admin.site.register(Patient)
