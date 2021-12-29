from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import EmployeeDetails
admin.site.register(EmployeeDetails,ImportExportModelAdmin)

class EmployeeAdmin(ImportExportModelAdmin):
 list_display = ('status','emp_id','resource_name','practice','department','reporting_managers','practice_lead','date_of_joining','location','mt_experience','non_mt_experience','gender','grade')
  
