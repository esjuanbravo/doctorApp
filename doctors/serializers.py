from rest_framework import serializers
from .models import Doctor, Department, DoctorAvailability, MedicalNote

class DoctorSerializers(serializers.ModelSerializer):
    departments = serializers.StringRelatedField(many=True)
    class Meta: 
        model = Doctor
        fields = ['id','first_name','last_name','specialization','departments','contant_number','address','email','biography','is_on_vacation']

class DepartmentSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Department
        fields = ['id','doctor','name']
        
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Accede al objeto Doctor relacionado y toma su __str__
        representation['doctor'] = str(instance.doctor) # O instance.doctor.first_name, etc.
        return representation
        
class DoctorAvailabilitySerializers(serializers.ModelSerializer):
    class Meta:
        model = DoctorAvailability
        fields = ['id','doctor','start_date','end_date','start_time','end_time']

class MedicalNoteSerializers(serializers.ModelSerializer):
    class Meta:
        model = MedicalNote
        fields = ['id','doctor','note','date']