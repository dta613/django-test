from .models import User_list, Patient, Patient_IWC, Patient_ANC,  Patient_Inpatient
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User_list
        fields = ('username', 'password')

class PatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient
        fields = ('Patient_firstname', 'Patient_lastname', '_all_',)

class Patient_ANCSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient_ANC
        fields = ('Patient_firstname', 'Patient_lastname')

class Patient_IWCSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient_IWC
        fields = ('Patient_firstname', 'Patient_lastname')

class Patient_InpatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patient_Inpatient
        fields = ('Patient_firstname', 'Patient_lastname')
