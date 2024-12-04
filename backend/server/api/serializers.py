from rest_framework import serializers
from .models import PatientDemographics, TestDemographics, RestingECG

class TestDemographicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestDemographics
        fields = ['acquisition_date']

class RestingECGSerializer(serializers.ModelSerializer):
    class Meta:
        model = RestingECG
        fields = [
            'ventricular_rate', 
            'atrial_rate', 
            'qrs_duration',
            'qt_interval', 
            'qt_corrected', 
            'r_axis', 
            't_axis'
        ]

class PatientDemographicsSerializer(serializers.ModelSerializer):
    TestDemographics = TestDemographicsSerializer(source='testdemographics_set', many=True)
    ECGMeasurements = RestingECGSerializer(source='restingecg_set', many=True)

    class Meta:
        model = PatientDemographics
        fields = [
            "patient_id",
            "gender",
            "last_name",
            "first_name",
            "TestDemographics",
            "ECGMeasurements",
        ]
