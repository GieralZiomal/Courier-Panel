# Generated by Django 3.2.16 on 2022-11-11 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_customuser_forma_wypłaty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='banknumer',
            field=models.CharField(default=True, max_length=100),
        ),
    ]