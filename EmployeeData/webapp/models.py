from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

class EmployeeDetails(models.Model):
    class Meta:
        verbose_name_plural = 'EmployeeDetails'
    
    GENDER_CHOICE = (("MALE", "Male"), ("FEMALE", "Female"))
    STATUS_CHOICE = (("ACTIVE","Active"),("INACTIVE","Inactive"))

    
    status = models.CharField(max_length=100,choices = STATUS_CHOICE,default='active')
    emp_id=models.IntegerField(primary_key=True)
    resource_name = models.CharField(max_length=100)
    practice = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    reporting_managers = models.CharField(max_length=100)
    practice_lead = models.CharField(max_length=100)
    date_of_joining = models.DateField(null=True)
    location = models.CharField(max_length=100)
    mt_experience = models.FloatField(max_length=100)
    non_mt_experience = models.FloatField(max_length=100)
    gender = models.CharField(max_length=100,choices = GENDER_CHOICE, default='active')
    grade = models.CharField(max_length=100)
    
    def __str__(self):
        return self.resource_name  


  # def save(self, *args, **kwargs):
    #     if self.resource_name.isalpha() is False:
    #         raise ValidationError(
    #         _('Name can only contain letters A-Z,a-z Not numbers.'),
    #         params={'resource_name': self.resource_name},
    #     )
    #     super(EmployeeDetails, self).save(*args, **kwargs)


    # def clean_resource_name(self):
    #     data = self.cleaned_data['resource_name']
    #     if not data.character():
    #        raise forms.ValidationError("resource name  should be in characters")
    #     return data

    # def verify_resource_name(self, resource_name):
    #     if not resource_name.isalpha():
    #         raise models.ValidationError("Name should be in character")


    
# def validate_name(resource_name):
#     print(resource_name.isalpha())

#     

