from rest_framework import serializers
from .models import Doctor, Department, DoctorAvailability, MedicalNote

class DoctorSerializers(serializers.ModelSerializer):
    departments = serializers.StringRelatedField(many=True)
    class Meta: 
        model = Doctor
        fields = ['id','first_name','last_name','specialization','departments','contant_number','address','email','biography','is_on_vacation']
        
        def validate_email(self, value):
            if '@holas.com'in value:
                return value
            raise serializers.ValidationError("El email debe contener '@holas.com'")

        def validate(self, attrs):
            if attrs['is_on_vacation'] and attrs['contact_number'] < 10:
                raise serializers.ValidationError("Si el doctor esta de vacaciones, debe tener un numero de contacto valido")
            return super().validate(attrs)

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