# Generated by Django 3.2.16 on 2022-11-11 14:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20221111_1454'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='dokument',
            field=models.FileField(default=0, upload_to=''),
        ),
        migrations.AlterField(
            model_name='rozliczenia',
            name='dataprzelewu',
            field=models.DateField(default=datetime.datetime(2022, 11, 11, 14, 55, 29, 361421, tzinfo=utc)),
        ),
    ]
