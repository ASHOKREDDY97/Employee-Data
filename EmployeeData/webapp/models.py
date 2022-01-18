from django.db import models
from django.core.exceptions import ValidationError
from django.db.models.enums import Choices
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
class EmployeeDetails(models.Model):
    class Meta:
        verbose_name_plural = 'EmployeeDetails'
    
    GENDER_CHOICE = (("MALE", "Male"), ("FEMALE", "Female"))
    STATUS_CHOICE = (("ACTIVE","Active"),("INACTIVE","Inactive"),("RESIGN","Resign"))
    PRACTICE_CHOICE = (("DIGITAL TRANSFORMATION","Digital Transformation"),)
    DEPARTMENT_CHOICE = (("DEVOPS","DevOps"),("ENTERPRISE APPLICATION DEVELOPMENT","Enterprise Application Development"),("UI","UI"),("CLOUD SOLUTIONS","Cloud Solutions"),("ENTERPRISE ARCHITECTURE","Enterprise Architecture"),("UX","UX"),("PRODUCT ENGINEERING","Product Engineering"),("MOBILITY","Mobility"),("PROFESSIONAL SERVICES","Professional Services"))
    PRACTICE_LEAD_CHOICE = (("SURESH TUKARAM SUTAR","Suresh Tukaram SUTAR"),("SAILAJA GUDALA","Sailaja GUDALA"),("SRINIVAS KANTTUGA","Srinivas KATTUNGA"),("ABHIJEET BHIKAJI PATIL","Abhijeet Bhikaji PATIL"),("SANJAY PARMANAND BATHEJA","Sanjay Parmanand BATHEJA"),("YYOMA DILIP PATHAK","Vyoma Dilip PATHAK"),("ABHIJEET HARISHCHANDRA ALONE","Abhijeet Harishchandra ALONE"),("NASIR AHMED R","Nasir Ahmed R"))

    status = models.CharField(max_length=100,choices = STATUS_CHOICE,null=True)
    emp_id=models.IntegerField(primary_key=True,null=False)
    resource_name = models.CharField(max_length=100,null=True)
    practice = models.CharField(max_length=100,choices=PRACTICE_CHOICE,default="Digital Transformation",null=True)
    department = models.CharField(max_length=100,choices=DEPARTMENT_CHOICE,null=True)
    reporting_managers = models.CharField(max_length=100,null=True)
    practice_lead = models.CharField(max_length=100,choices=PRACTICE_LEAD_CHOICE,null=True)
    date_of_joining = models.DateField(blank=True , null=True)
    location = models.CharField(max_length=100,null=True)
    mt_experience = models.FloatField(max_length=100,null=True)
    non_mt_experience = models.FloatField(max_length=100,blank=True , null=True)
    gender = models.CharField(max_length=100,choices=GENDER_CHOICE,null=True)
    grade = models.CharField(max_length=100,blank=True , null=True)

    def __str__(self):
        return self.resource_name  


class EmployeeUserDetails(models.Model):
    class Meta:
        verbose_name_plural = 'EmployeeUserDetails'
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    form_submitted = models.BooleanField(blank=True, null=True, default=False)
    





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

