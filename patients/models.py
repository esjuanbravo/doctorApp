from django.db import models

# Create your models here.
class Patient(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    date_of_birth = models.DateField()
    address  = models.TextField( null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
    
class Insurance(models.Model):
    patient = models.ForeignKey(Patient, related_name='insurances', on_delete=models.CASCADE)
    provider = models.CharField(max_length=100)
    policy_number = models.CharField(max_length=50, unique=True)
    coverage_details = models.TextField()

    def __str__(self):
        return f"{self.provider} - {self.policy_number} ({self.patient})" 
    
class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, related_name='medical_records', on_delete=models.CASCADE)
    date = models.DateField()
    diagnosis = models.CharField()
    tratament = models.TextField()
    follow_up_date = models.DateField()
    
    def __str__(self):
        return f'{self.patient} - {self.diagnosis}'