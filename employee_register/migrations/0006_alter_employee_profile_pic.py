# Generated by Django 4.1 on 2022-09-07 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0005_remove_employee_picture_employee_profile_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='profile_pic',
            field=models.FileField(upload_to='media/images'),
        ),
    ]