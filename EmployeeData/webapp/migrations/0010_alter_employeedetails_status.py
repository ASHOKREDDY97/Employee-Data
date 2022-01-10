# Generated by Django 4.0 on 2022-01-03 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0009_alter_employeedetails_date_of_joining_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeedetails',
            name='status',
            field=models.CharField(blank=True, choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive'), ('RESIGN', 'Resign')], default='active', max_length=100, null=True),
        ),
    ]