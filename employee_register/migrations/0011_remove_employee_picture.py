# Generated by Django 4.1 on 2022-09-07 06:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0010_employee_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='picture',
        ),
    ]
