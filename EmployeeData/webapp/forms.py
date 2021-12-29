from django import forms
from django.db.models import fields
from django.forms import ModelForm
from .models import EmployeeDetails
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms.fields import DateField
from django.core.exceptions import ValidationError


class EmployeeForm(ModelForm):
 
    class Meta:
        model = EmployeeDetails
        fields = ('status','emp_id','resource_name','practice','department','reporting_managers','practice_lead','date_of_joining','location','mt_experience','non_mt_experience','gender','grade')
        
        widgets ={
            
            'status':forms.Select(attrs={'class':'form-control',}),
            'emp_id':forms.NumberInput(attrs={'class':'form-control',}),
            'resource_name':forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}),
            'practice':forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}),
            'department':forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}),
            'reporting_managers':forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}),
            'practice_lead':forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}),
            'date_of_joining':forms.widgets.DateInput(attrs={'type': 'date'}),
            'location':forms.TextInput(attrs={'class':'form-control' , 'autocomplete': 'off','pattern':'[A-Za-z ]+', 'title':'Enter Characters Only '}),
            'mt_experience':forms.NumberInput(attrs={'class':'form-control'}),
            'non_mt_experience':forms.NumberInput(attrs={'class':'form-control'}),
            'gender':forms.Select(attrs={'class':'form-control'}),
            'grade':forms.TextInput(attrs={'class':'form-control'}) 
        }

        # def clean_emp(self,emp_id):
        #     for instance.emp_id in EmployeeDetails.all():
        #         raise forms.ValidationError('Employee with same Id is already Exists' + emp_id)
        #     return emp_id

           

        # def save(self, commit=True):    
        #     m = super(EmployeeForm, self).save(commit=False)
        #     # do custom stuff
        #     if commit:
        #         m.save()
        #     return m


        # def clean_emp_id(self):
        #     emp_id = self.cleaned_data['emp_id']
        #     try:
        #         EmployeeDetails.objects.get(emp_id=emp_id)
        #     except User.DoesNotExist:
        #         return emp_id
        #     raise forms.ValidationError("User with same Employee Id already exist")


    #     for instance in EmployeeDetails.objects.all():
    #         if instance.emp_id == emp_id:
    #       raise forms.ValidationError('Employee Id  is already created')
    # return emp_id


    
    # def clean_emp_id(self):
    #     '''
    #     Verify emp_id is available.
    #     '''
    #     emp_id = self.cleaned_data.get('emp_id')
    #     qs = EmployeeDetails.objects.filter(emp_id=emp_id)
    #     if qs.exists():
    #         raise forms.ValidationError("Employye Id is already Exists")
    #     return emp_id


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']


    

                                                               