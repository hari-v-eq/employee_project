# Generated by Django 4.1 on 2022-09-07 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_register', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='picture',
            field=models.ImageField(default='none', upload_to=''),
        ),
    ]
