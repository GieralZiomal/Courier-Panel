# Generated by Django 3.2.16 on 2022-11-11 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20221111_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='Forma_Wypłaty',
            field=models.CharField(blank=True, choices=[('gotówka', 'gotówka'), ('przelew', 'przelew')], default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='banknumer',
            field=models.CharField(blank=True, default=0, max_length=100),
            preserve_default=False,
        ),
    ]
