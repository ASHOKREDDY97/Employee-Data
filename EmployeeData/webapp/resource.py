from import_export import resources
from.models import EmployeeDetails

class EmployeeResource(resources.ModelResource):
    class meta:
        model=EmployeeDetails