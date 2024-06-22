from django.contrib import admin
from .models import employee
from .models import employee_role
from .models import employee_dept
from .models2 import Branch
from .models2 import Branch_floor
from .models2 import Branch_employee

admin.site.register(employee)
admin.site.register(employee_role)
admin.site.register(employee_dept)
admin.site.register(Branch)
admin.site.register(Branch_floor)
admin.site.register(Branch_employee)