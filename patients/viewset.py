from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Patient, Insurance, MedicalRecord
from .serializers import PatientSerializers, InsuranceSerializers, MedicalRecordSerializers

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializers
    
     # acion para ver historial medico
    @action(detail=True, methods=['GET'], url_path='show-medical-record')
    def show_medical_record(self, request, pk):
        patient = self.get_object()
        medical_record = MedicalRecord.objects.filter(patient=patient)
        serializers = MedicalRecordSerializers(medical_record, many=True)
        return Response(serializers.data)
        
    
class InsuranceViewSet(viewsets.ModelViewSet):
    queryset = Insurance.objects.all()
    serializer_class = InsuranceSerializers
    
class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializers
    