# Generated by Django 3.2.16 on 2022-11-11 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Rozliczenia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datedate', models.TextField(default=0)),
                ('money', models.TextField(default=0)),
                ('przelewwykonany', models.BooleanField(default=False)),
                ('dlakogo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pasport', models.FileField(default=0, upload_to='')),
                ('kartapobytu', models.FileField(default=0, upload_to='')),
                ('legitimation', models.FileField(default=0, upload_to='')),
                ('study', models.FileField(default=0, upload_to='')),
                ('dlakogo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
