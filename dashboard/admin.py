from django.contrib import admin
from dashboard.models import Patient
# Register your models here.

class PatientAdmin(admin.ModelAdmin):
    list_display = ('Patient_name', 'age', 'location', 'condition', 'medication', 'initial_visit', 'followup_appt', 'reminder_freq')

admin.site.register(Patient, PatientAdmin)
