from rest_framework import serializers
from .models2 import Branch
from .models2 import Branch_employee
from .models2 import Branch_floor

class BranchSerializers(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['id','name','address','Branch_employees','Branch_floor']


class Branch_employeeSerializers(serializers.ModelSerializer):
    class Meta:
        model = Branch_employee
        fields = ['id', 'employee_nos']

class Branch_floorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Branch_floor
        fields = ['id','floor']

class Branch_filterSerializers(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['Branch_employees','Branch_floor']