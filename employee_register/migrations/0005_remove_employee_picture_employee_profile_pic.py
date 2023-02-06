# Generated by Django 4.1 on 2022-09-07 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0004_alter_employee_picture'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='picture',
        ),
        migrations.AddField(
            model_name='employee',
            name='profile_pic',
            field=models.FileField(default='media/default.png', upload_to='media/images'),
        ),
    ]
