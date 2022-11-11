from django.db import models
from django.contrib.auth.models import User
from users.models import CustomUser
from django.utils import timezone

# Create your models here.
class Documents(models.Model):
    dlakogo = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    TYP_DOKUMENTU = (
        ('Pasport', 'Paszport'),
        ('Legitimation', 'Legitymacja'),
        ('Visa/Residence Card', 'Wiza/Karta Pobytu'),
        ('Certificate of study', 'Zaświadczenie o studiach'),
    )
    typ_dokumentu = models.CharField(max_length=20, choices=TYP_DOKUMENTU)
    dokument = models.FileField(default=0, upload_to="media")
    
    def __str__(self):
        return "Dokument"

class Rozliczenia(models.Model):
    dlakogo = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    datedate = models.TextField(default=0)
    money = models.TextField(default=0)
    appname = models.TextField(default=0)
    Vat = models.TextField(default=0)
    Prowizja_Partnera = models.TextField(default=0)
    Koszty_ZUS_I_Podatki = models.TextField(default=0)
    Inne_Koszty = models.TextField(default=0)
    Wypłata_Z_Tytułu_Najmu = models.TextField(default=0)
    Wypłata_Z_Tytułu_Zlecenia = models.TextField(default=0)
    Wypłata_Suma = models.TextField(default=0)

    dataprzelewu = models.DateField(default=timezone.now())
    przelewwykonany = models.BooleanField(default=False)

    def __str__(self):
        return "Rozliczenie"