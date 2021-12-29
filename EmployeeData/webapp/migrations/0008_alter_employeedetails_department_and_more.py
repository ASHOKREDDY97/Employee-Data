# Generated by Django 4.0 on 2021-12-20 06:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0007_alter_employeedetails_department_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetails',
            name='department',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female')], default='active', max_length=100),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='location',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='practice',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='practice_lead',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='reporting_managers',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='resource_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='employeedetails',
            name='status',
            field=models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')], default='active', max_length=100),
        ),
    ]
