from rest_framework.routers import DefaultRouter
from .viewset import DoctorViewSet, DepartmentViewSet, DoctorAvailabilityViewSet, MedicalNoteViewSet


router = DefaultRouter()
router.register('doctor', DoctorViewSet)
router.register('departamento', DepartmentViewSet)
router.register('doctor-disponible', DoctorAvailabilityViewSet)
router.register('nota-medica', MedicalNoteViewSet)
urlpatterns = router.urls
