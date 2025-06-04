from rest_framework.routers import DefaultRouter
from .viewset import PatientViewSet, InsuranceViewSet, MedicalRecordViewSet

router = DefaultRouter()
router.register('paciente', PatientViewSet)
router.register('seguro', InsuranceViewSet)
router.register('historial-medico', MedicalRecordViewSet)
urlpatterns = router.urls
