from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active',)
    list_filter = ('email', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('User Data', {'fields': ('pesel', 'numer_dokumentu', 'aplikacja', 'imie', 'nazwisko', 'data_urodzenia', 'ulica', 'kod_pocztowy', 'numer_domu', 'miasto', 'banknumer', 'srodek_transportu', 'Forma_Wypłaty')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
        ('Dane Dotyczące Umowy', {"fields": ('Jestem_Z_Ukrainy', 'Mam_Kartę_Polaka', 'Rezydent_EU', "Karta_Pobytu_Połączenia_Z_Rodzina", "Wiza_21_lub_23_BiznesHub", "Obywatel_EU")})
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)