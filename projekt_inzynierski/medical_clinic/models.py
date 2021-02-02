from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    class Meta:
        permissions = [
            ("is_administration", "Administration"),
            ("is_doctor", "Doctor"),
            ("is_reception", "Receptionist"),
        ]

class Patient(models.Model):
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    pesel = models.CharField(max_length=20, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)
    sex = models.CharField(max_length=20, blank=True)
    birth_date= models.DateField()


class PatientHistory(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    entry = models.TextField(max_length=5000, blank=True)
    medicine = models.CharField(max_length=500, blank=True)
    dose = models.CharField(max_length=500, blank=True)


class Visit(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
