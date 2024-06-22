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
    email = models.EmailField(max_length=100, unique= True)
    #created_at = models.DateTimeField(auto_now_add=True)
    #updated_at = models.DateTimeField(auto_now=True)
    employee_role = models.ForeignKey(employee_role, null = True,on_delete= models.SET_NULL,blank=True)
    employee_dept = models.ForeignKey(employee_dept, null = True,on_delete= models.SET_NULL,blank=True)
    password = models.CharField(max_length=20,default ="guest",null = False)
    #email2 = models.EmailField(max_length=100,null = True)
    #login api
    #login api next email and password auth
    #email avail or not
    #if email corr check passw
    #if ok show credittionals
    


    def __str__(self):
        return self.name


