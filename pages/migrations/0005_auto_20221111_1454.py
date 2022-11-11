# Generated by Django 3.2.16 on 2022-11-11 14:54

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0004_alter_rozliczenia_dataprzelewu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='documents',
            name='kartapobytu',
        ),
        migrations.RemoveField(
            model_name='documents',
            name='legitimation',
        ),
        migrations.RemoveField(
            model_name='documents',
            name='pasport',
        ),
        migrations.RemoveField(
            model_name='documents',
            name='study',
        ),
        migrations.AddField(
            model_name='documents',
            name='typ_dokumentu',
            field=models.CharField(choices=[('pasport', 'Paszport'), ('legitimation', 'Legitymacja'), ('wiza', 'Wiza/Karta Pobytu'), ('study', 'Zaświadczenie o studiach')], default=0, max_length=12),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='rozliczenia',
            name='dataprzelewu',
            field=models.DateField(default=datetime.datetime(2022, 11, 11, 14, 54, 43, 400804, tzinfo=utc)),
        ),
    ]