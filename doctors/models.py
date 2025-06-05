from django.db import models
from django.utils import timezone

# Create your models here.
class Doctor(models.Model):
    first_name = models.CharField()
    last_name = models.CharField()
    specialization = models.CharField(max_length=100)
    contant_number = models.TextField()
    start_of_career = models.DateField(default=timezone.now)
    address = models.TextField()
    email = models.EmailField()
    biography = models.TextField()
    is_on_vacation = models.BooleanField(default=False)
    
    def __str__(self):
        return f'Dr. {self.first_name} {self.last_name}'
    
    
class Department(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='departments', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return f'{self.name}'
    
class DoctorAvailability(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='availabilities', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    
    

class MedicalNote(models.Model):
    doctor = models.ForeignKey(Doctor, related_name='medical_notes', on_delete=models.CASCADE)
    note = models.TextField()
    date = models.DateField()
