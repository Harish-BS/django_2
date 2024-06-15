from rest_framework import serializers 
from .models import employee
from .models import employee_role
from .models import employee_dept

class employeesSerializers(serializers.ModelSerializer):
    class Meta:
        model = employee
        fields = ['id', 'name', 'email','employee_role','employee_dept']

class employee_roleSerializers(serializers.ModelSerializer):
    class Meta:
        model = employee_role
        fields = ['id','role']

class employee_deptSerializers(serializers.ModelSerializer):
    class Meta:
        model = employee_dept
        fields = ['id','dept']