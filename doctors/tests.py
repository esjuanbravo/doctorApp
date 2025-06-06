from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from patients.models import Patient
from doctors.models import Doctor

class DoctorViewSetTests(TestCase):
    def setUp(self):
        #con estos datos se va a simular un request para el test
        #accedemos a las funciones del orm
       self.patient = Patient.objects.create(
            first_name='epatrocleo',
            last_name='agustins',
            email='esepatrocleo@hoals.com',
            phone_number='1234567890',
            date_of_birth='2000-02-12',
            medical_history='niguan',
            address='vive e la calle ',
       )
       self.doctor = Doctor.objects.create(
            first_name='Juan',
            last_name='Bravo',
            specialization='dentista',
            contant_number='1234567890',
            start_of_career='2000-12-27',
            address='su casa',
            email='esjuan@holas.com',
            biography='el es doctor',
            is_on_vacation=False,
       )
       self.client = APIClient()
       
       # a partir de aqui se pueden hacer la pruevas nesesarias 
       
    def test_list_should_return_200(self):
       url = reverse('doctor-appointments', kwargs={'pk': self.doctor.id})
       response = self.client.get(url)
       self.assertEqual(response.status_code,status.HTTP_403_FORBIDDEN)       
           