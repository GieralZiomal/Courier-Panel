# Generated by Django 3.2.16 on 2022-11-11 11:07

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now)),
                ('pesel', models.CharField(max_length=100)),
                ('aplikacja', models.CharField(max_length=100)),
                ('imie', models.CharField(max_length=100)),
                ('nazwisko', models.CharField(max_length=100)),
                ('numer_dokumentu', models.CharField(max_length=100)),
                ('data_urodzenia', models.CharField(max_length=100)),
                ('ulica', models.CharField(max_length=100)),
                ('numer_domu', models.CharField(max_length=100)),
                ('kod_pocztowy', models.CharField(max_length=100)),
                ('miasto', models.CharField(max_length=100)),
                ('banknumer', models.CharField(max_length=100)),
                ('srodek_transportu', models.CharField(choices=[('samochód', 'samochód'), ('hulajnoga', 'hulajnoga'), ('rower', 'rower'), ('moped', 'moped')], max_length=100)),
                ('Jestem_Z_Ukrainy', models.CharField(choices=[('tak', 'tak'), ('nie', 'nie')], max_length=100)),
                ('Mam_Kartę_Polaka', models.CharField(choices=[('tak', 'tak'), ('nie', 'nie')], max_length=100)),
                ('Rezydent_EU', models.CharField(choices=[('tak', 'tak'), ('nie', 'nie')], max_length=100)),
                ('Karta_Pobytu_Połączenia_Z_Rodzina', models.CharField(choices=[('tak', 'tak'), ('nie', 'nie')], max_length=100)),
                ('Wiza_21_lub_23_BiznesHub', models.CharField(choices=[('tak', 'tak'), ('nie', 'nie')], max_length=100)),
                ('Obywatel_EU', models.CharField(choices=[('tak', 'tak'), ('nie', 'nie')], max_length=100)),
                ('Forma_Wypłaty', models.CharField(choices=[('gotówka', 'gotówka'), ('przelew', 'przelew')], max_length=100)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
