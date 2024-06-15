from django.db import models

class employee_role(models.Model):
    role = models.CharField(max_length=100, null = True)
    def __str__(self):
        return self.role
    

class employee_dept(models.Model):
    dept = models.CharField(max_length=100,null = True)
    def __str__(self):
        return self.dept
#comment    

class employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=30, unique= True)
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)
    employee_role = models.ForeignKey(employee_role, null = True,on_delete= models.SET_NULL)
    employee_dept = models.ForeignKey(employee_dept, null = True,on_delete= models.SET_NULL)

    def __str__(self):
        return self.name