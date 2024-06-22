from django.db import models

class Branch_floor(models.Model):
    floor = models.CharField(max_length=100,null=True)

    def __str__(self):
        return 'floor-> '+self.floor


class Branch_employee(models.Model):
    employee_nos = models.CharField(max_length=10000,null=True)

    def __str__(self):
        return "emp_nos-> "+self.employee_nos


class Branch(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100,null=True,unique=True)
    Branch_employees = models.ForeignKey(Branch_employee,null=True,on_delete=models.SET_NULL,blank=True)
    Branch_floor = models.ForeignKey(Branch_floor,null=True,on_delete=models.SET_NULL,blank=True)

    def __str__(self):
        return self.name

