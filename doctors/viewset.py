from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsDoctor
from .models import Doctor, Department, DoctorAvailability, MedicalNote
from .serializers import DoctorSerializers, DepartmentSerializers, DoctorAvailabilitySerializers, MedicalNoteSerializers
from bookings.serializers import AppointmentSerializer
from bookings.models import Appointment



class DoctorViewSet(viewsets.ModelViewSet):
    """
    vista con dos acciones una para decirle que tiene vacacione en el sistema habilitadas 
    y otras para quitarle dichas vacaiones    
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializers
    # con esto solo se puede tener acceso si esta login y ser doctor
    permission_classes = [IsAuthenticatedOrReadOnly, IsDoctor]    
    @action(['POST'], detail=True, url_path='set-on-vacation')
    def set_on_vacation(self, request, pk):
       doctor = self.get_object()
       doctor.is_on_vacation = True
       doctor.save()
       return Response({"status":'esta el doctor de vacaciones'})
   
    @action(['POST'], detail=True, url_path='set-off-vacation')
    def set_off_vacation(self, request, pk):
       doctor = self.get_object()
       doctor.is_on_vacation = False
       doctor.save()
       return Response({"status":'el doctor ya no esta de vacaciones'})
   # para que el doctor pueda hacer cita para los 
    @action(['POST', 'GET'], detail=True, serializer_class=AppointmentSerializer)
    def appointments(self, request, pk):
        doctor = self.get_object()

        if request.method == 'POST':
            data = request.data.copy()
            data['doctor'] = doctor.id
            serializer = AppointmentSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        if request.method == 'GET':
            appointments = Appointment.objects.filter(doctor=doctor)
            serializer = AppointmentSerializer(appointments, many=True)
            return Response(serializer.data)
            
    
    
class DepartmentViewSet(viewsets.ModelViewSet):
    
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers
    
class DoctorAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = DoctorAvailability.objects.all()
    serializer_class = DoctorAvailabilitySerializers
    
class MedicalNoteViewSet(viewsets.ModelViewSet):
    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNoteSerializers