from django.contrib import admin
from .models import employee
from .models import employee_role
from .models import employee_dept

admin.site.register(employee)
admin.site.register(employee_role)
admin.site.register(employee_dept)