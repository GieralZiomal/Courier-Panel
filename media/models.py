from django.db import models
from django.contrib.auth.models import User

class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pesel = models.CharField(max_length=100)
    aplikacja= models.CharField(max_length=100)
    imie = models.CharField(max_length=100)
    nazwisko = models.CharField(max_length=100)
    numer_dokumentu = models.CharField(max_length=100)
    data_urodzenia = models.CharField(max_length=100)
    ulica = models.CharField(max_length=100)
    numer_domu = models.CharField(max_length=100)
    kod_pocztowy = models.CharField(max_length=100)
    miasto = models.CharField(max_length=100)