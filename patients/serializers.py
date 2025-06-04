from rest_framework import serializers
from .models import Patient, Insurance, MedicalRecord

class PatientSerializers(serializers.ModelField):
    class Meta:
        model = Patient
        fields = ['id','first_name','last_name','email','phone_number','date_of_birth','address']
        
class InsuranceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = ['id','patient','provider','policy_number','coverage_details']
        
class MedicalRecordSerializers(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = ['id','patient','date','diagnosis','tratament','follow_up_date']