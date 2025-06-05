from rest_framework import serializers
from datetime import date
from .models import Patient, Insurance, MedicalRecord
from bookings.serializers import AppointmentSerializers

class PatientSerializers(serializers.ModelSerializer):
    # instanciamos la clase serializadora 
    appointments = AppointmentSerializers(many=True, read_only=True) # es many hace que tomo en cuenta a todos los objetos
    age = serializers.SerializerMethodField()    
    class Meta:
        model = Patient
        fields = ['id','first_name','last_name','age','email','phone_number','date_of_birth','address','medical_history','appointments']
    
    # este nombre es porque no ese definio en age = serializers.SerializerMethodField()
    def get_age(self, obj):
        age_dt = date.today() - obj.date_of_birth
        return age_dt.days // 365
        
        
class InsuranceSerializers(serializers.ModelSerializer):
    class Meta:
        model = Insurance
        fields = ['id','patient','provider','policy_number','coverage_details']
        
class MedicalRecordSerializers(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = ['id','patient','date','diagnosis','tratament','follow_up_date']