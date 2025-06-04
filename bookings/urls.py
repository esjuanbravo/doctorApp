from rest_framework.routers import DefaultRouter
from .viewsets import AppointmentViewSet, MedicalNoteViewSet

router = DefaultRouter()
router.register('cita', AppointmentViewSet)
router.register('nota-medica',MedicalNoteViewSet)
urlpatterns = router.urls
