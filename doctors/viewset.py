from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsDoctor
from .models import Doctor, Department, DoctorAvailability, MedicalNote
from .serializers import DoctorSerializers, DepartmentSerializers, DoctorAvailabilitySerializers, MedicalNoteSerializers

class DoctorViewSet(viewsets.ModelViewSet):
    """
    vista con dos acciones una para decirle que tiene vacacione en el sistema habilitadas 
    y otras para quitarle dichas vacaiones    
    """
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializers
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
    
    
class DepartmentViewSet(viewsets.ModelViewSet):
    
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializers
    
class DoctorAvailabilityViewSet(viewsets.ModelViewSet):
    queryset = DoctorAvailability.objects.all()
    serializer_class = DoctorAvailabilitySerializers
    
class MedicalNoteViewSet(viewsets.ModelViewSet):
    queryset = MedicalNote.objects.all()
    serializer_class = MedicalNoteSerializers