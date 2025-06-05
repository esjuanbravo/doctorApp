from rest_framework import serializers
from datetime import date
from .models import Doctor, Department, DoctorAvailability, MedicalNote
from bookings.serializers import AppointmentSerializers

class DoctorSerializers(serializers.ModelSerializer):
    departments = serializers.StringRelatedField(many=True)
    appointments = AppointmentSerializers(many=True, read_only=True)
    time_of_experience = serializers.SerializerMethodField()
    class Meta: 
        model = Doctor
        fields = ['id','first_name','last_name','specialization','departments','contant_number','address','email','biography','is_on_vacation','appointments']
        
        # el como validar informacion de los campos, esta en la prate de de los serializer ya que no tedria sentido 
        # ya que despues de convertir modelos a informacion dijerible puede haber logica dentro de estos cuerpos 
        
        def validate_email(self, value): # para validar correos

            if '@holas.com'in value:
                return value
            raise serializers.ValidationError("El email debe contener '@holas.com'")

        def validate(self, attrs): # para validar numeros telefonicos 
            if attrs['is_on_vacation'] and attrs['contact_number'] < 10:
                raise serializers.ValidationError("Si el doctor esta de vacaciones, debe tener un numero de contacto valido")
            return super().validate(attrs)
        
        def get_time_of_experience(self, obj):
            return (date.today() - obj.start_of_career).days // 365

class DepartmentSerializers(serializers.ModelSerializer):
    class Meta: 
        model = Department
        fields = ['id','doctor','name']
    
    # metodo para acceder a las reaciones de definidas en los modelos 
    def to_representation(self, instance):
        # recuerda que el motodo super() acceder a metodos de clases padres desde las hijas
        #
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