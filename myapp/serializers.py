from .models import user_list, patient, patient_iwc, patient_anc,  patient_inpatient
from rest_framework import serializers


class userSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = user_list
        fields = ('username', 'password')

class patientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = patient
        fields = ('patient_firstname', 'patient_lastname', '_all_',)

class patient_ancSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = patient_anc
        fields = ('patient_firstname', 'patient_lastname')

class patient_iwcSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = patient_iwc
        fields = ('patient_firstname', 'patient_lastname')

class patient_inpatientSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = patient_inpatient
        fields = ('Patient_firstname', 'Patient_lastname')
