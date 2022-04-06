from django.http import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .resource import EmployeeResource
from .forms import EmployeeForm,CreateUserForm
from .models import EmployeeDetails,EmployeeUserDetails
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from tablib import Dataset
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError

# Upload Data from Excel Sheet
@login_required(login_url='login')
def dataupload(request):
 if request.user.is_superuser:
    if request.method=='POST':
        employee_resource=EmployeeResource()
        dataset=Dataset()
        print(request)
        print(request.FILES.get('myfile'))
        
        new_employee= request.FILES['myfile']
        print(new_employee)

        if not new_employee.name.endswith('xlsx'):
            messages.info(request,'wrong format')
            return render(request,'upload.html')

        imported_data=dataset.load(new_employee.read(),format='xlsx')
        for data in imported_data:
            value=EmployeeDetails(
                data[0],
                data[1],
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
                data[10],
                data[11],
                data[12],
            )
            value.save()    
        messages.success(request,'file is uploaded')
    return render(request,'upload.html')
 else:
        return redirect('addnew')

# Employee Register
def register(request):
    if request.user.is_authenticated:
        return redirect('index')
    else:
        form = CreateUserForm()
        if request.method =='POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request,'Account Was Created for ' +user)
                return redirect('login')
        return render(request, 'register.html', {'form': form})

# Employee Login
def loginpage(request, form=None):
    if request.user.is_authenticated:
        print(request.user.is_superuser)
        if request.user.is_superuser:
            return redirect('index')
        else:
            return redirect('addnew')

    else:
        if request.method == 'POST':
            username =request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                if request.user.is_superuser:
                    return redirect('index')
                else:
                    return redirect('addnew')
            else:
                messages.info(request, 'username OR password is incorrect')
        return render(request, 'login.html', {'form': form})

# Employee Logout
def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def index(request):
    if request.user.is_superuser:
        filter_tuple = ("inactive", "INACTIVE")
        employees = EmployeeDetails.objects.exclude(status__in=filter_tuple) 
        return render(request, "show.html", {'employees': employees})
    else:
        return redirect('addnew')

@login_required(login_url='login')
def inactive_employees(request):
    if request.user.is_superuser:
        filter_tuple = ("inactive", "INACTIVE")
        employees = EmployeeDetails.objects.filter(status__in=filter_tuple) 
        return render(request, "show.html", {'employees': employees})
    else:
        return redirect('addnew')  
    
    
# POST method
@login_required(login_url='login')
def addnew(request):  
    if request.method == "POST":  
        form = EmployeeForm(request.POST)  
        if form.is_valid():
            user = EmployeeDetails.objects.filter(emp_id=form.cleaned_data['emp_id'])
            if user.exists():
                messages.error(request,'Employee with same Id is already Exists')
                return render(request,'index.html',{'form':form})

            try:  
               
                if request.user.is_superuser:
                    pass
                else:
                    qs,created = EmployeeUserDetails.objects.get_or_create(user = request.user,form_submitted = True)
                    if not created:
                        messages.success(request,'Form has been already submitted')
                        return render(request,'index.html',{'form':form})
                form.save()

                messages.success(request,'Form has been submitted')
                return redirect('/')  
            except:
                pass 
    else:  
        form = EmployeeForm()
    return render(request,'index.html',{'form':form})

# Edit and Update method
@login_required(login_url=login)
def edit(request, id):                         
    employee_obj = EmployeeDetails.objects.get(emp_id=id) 
            
    if request.method == 'POST':
        print(request.POST)
        form = EmployeeForm(request.POST, instance=employee_obj)
        print(form)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = EmployeeForm(instance=employee_obj)
    return render(request, 'edit.html', {'employee': form, 'id': id})

# Delete Method
def destroy(request, id):
    employee = EmployeeDetails.objects.get(emp_id=id)  
    employee.delete()  
    return redirect("/") 

def submit(request):
     return render(request, 'submit.html')