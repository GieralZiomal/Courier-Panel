# Generated by Django 3.2.16 on 2022-11-11 16:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0012_alter_rozliczenia_dataprzelewu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rozliczenia',
            name='dataprzelewu',
            field=models.DateField(default=datetime.datetime(2022, 11, 11, 16, 41, 23, 869514, tzinfo=utc)),
        ),
    ]
