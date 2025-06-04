from rest_framework import viewsets
from .models import Appointment, MedicalNote
from .serializers import AppointmentSerializers, MedicalNoteSerializers

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializers
    
class MedicalNoteViewSet(viewsets.ModelViewSet):
    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNoteSerializers