# Generated by Django 4.0 on 2021-12-17 06:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0005_alter_employeedetails_s_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employeedetails',
            name='s_no',
        ),
    ]
