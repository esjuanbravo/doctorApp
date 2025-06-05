# Los serializer son componentes de Django Rest Framework que sirven para tranformar datos
# complejos como modelos o instancias a formatos de rest como json u otros.

from rest_framework import serializers
from .models import Appointment, MedicalNote

class AppointmentSerializers(serializers.ModelSerializer):
    patient = serializers.StringRelatedField()
    doctor = serializers.StringRelatedField()
    class Meta:
        model = Appointment
        fields = ['id','patient','doctor','appointment_date','appointment_time','notes','status']
        
        
class MedicalNoteSerializers(serializers.ModelField):
    class Meta:
        model = MedicalNote
        fields = ['id','appointment','note','date']
