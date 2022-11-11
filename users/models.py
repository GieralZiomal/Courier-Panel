from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
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
    banknumer = models.CharField(max_length=100, blank=True, null=True)
    verificated = models.BooleanField(default=False)

    SRODEK = (

        ('samochód', ('samochód')),
        ('hulajnoga', ('hulajnoga')),
        ('rower', ('rower')),
        ('moped', ('moped')),

    )

    TAKNIE = (

        ('tak', ('tak')),
        ('nie', ('nie'))

    )

    FORMAWYPŁATY = (

        ('gotówka', ('gotówka')),
        ('przelew', ('przelew')),

    )

    srodek_transportu = models.CharField(max_length=100, choices=SRODEK)
    Jestem_Z_Ukrainy  = models.CharField(max_length=100, choices=TAKNIE)
    Mam_Kartę_Polaka  = models.CharField(max_length=100, choices=TAKNIE)
    Rezydent_EU = models.CharField(max_length=100, choices=TAKNIE)
    Karta_Pobytu_Połączenia_Z_Rodzina = models.CharField(max_length=100, choices=TAKNIE)
    Wiza_21_lub_23_BiznesHub = models.CharField(max_length=100, choices=TAKNIE)
    Obywatel_EU = models.CharField(max_length=100, choices=TAKNIE)
    Forma_Wypłaty = models.CharField(max_length=100, choices=FORMAWYPŁATY,blank=True, null=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email

SRODEK = (

        ('samochód', ('samochód')),
        ('hulajnoga', ('hulajnoga')),
        ('rower', ('rower')),
        ('moped', ('moped')),

    )

TAKNIE = (

        ('tak', ('tak')),
        ('nie', ('nie'))

    )

FORMAWYPŁATY = (

        ('gotówka', ('gotówka')),
        ('przelew', ('przelew')),

    )