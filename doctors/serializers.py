from rest_framework import serializers
from .models import Doctor, Department, DoctorAvailability, MedicalNote

class DoctorSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Doctor
        fields = ['id','first_name','last_name','specialization','contant_number','address','email','biography','is_on_vacation']

class DepartmentSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Department
        fields = ['id','doctor','name','description']
        
class DoctorAvailabilitySerializers(serializers.ModelSerializer):
    class Meta:
        model = DoctorAvailability
        fields = ['id','doctor','start_date','end_date','start_time','end_time']

class MedicalNoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = ['id','doctor','note','date']