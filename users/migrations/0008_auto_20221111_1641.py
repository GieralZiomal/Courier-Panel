# Generated by Django 3.2.16 on 2022-11-11 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_alter_customuser_banknumer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='Forma_Wypłaty',
            field=models.CharField(choices=[('gotówka', 'gotówka'), ('przelew', 'przelew')], default=0, max_length=100),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='banknumer',
            field=models.CharField(default=0, max_length=100),
        ),
    ]