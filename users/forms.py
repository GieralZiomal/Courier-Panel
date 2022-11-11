from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms
from .models import CustomUser, SRODEK, TAKNIE, FORMAWYPŁATY

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email','pesel', 'numer_dokumentu', 'aplikacja', 'imie', 'nazwisko', 'data_urodzenia', 'ulica', 'kod_pocztowy', 'numer_domu', 'miasto')

        srodek_transportu = forms.ChoiceField(choices=SRODEK)
        Jestem_Z_Ukrainy  = forms.ChoiceField(choices=TAKNIE)
        Mam_Kartę_Polaka  = forms.ChoiceField(choices=TAKNIE)
        Rezydent_EU = forms.ChoiceField(choices=TAKNIE)
        Karta_Pobytu_Połączenia_Z_Rodzina = forms.ChoiceField(choices=TAKNIE)
        Wiza_21_lub_23_BiznesHub = forms.ChoiceField(choices=TAKNIE)
        Obywatel_EU = forms.ChoiceField(choices=TAKNIE)
        Forma_Wypłaty = forms.ChoiceField(choices=FORMAWYPŁATY)