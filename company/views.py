from django.http import HttpResponse
from django.shortcuts import render
from .models import employee
from .serializers import employeesSerializers
from django.http import JsonResponse
from rest_framework.decorators import api_view 
from django.contrib.auth import authenticate, login
from rest_framework.response import Response 
from rest_framework import status 
from .models import employee_role
from .models import employee_dept
from .serializers import employee_roleSerializers
from .serializers import employee_deptSerializers
from .serializers import employee_filterSerializers
from .serializers2 import BranchSerializers
from .serializers2 import Branch_employeeSerializers
from .serializers2 import Branch_floorSerializers
from .serializers2 import Branch_filterSerializers
from .serializers import LoginSerializer
from django.core.paginator import Paginator
from .models2 import Branch
from .models2 import Branch_employee
from .models2 import Branch_floor


def home(request):
    Employee = employee.objects.all()
    employee_paginator = Paginator(Employee, 5)
    page_num = request.GET.get('page')
    page =  employee_paginator.get_page(page_num)
    context = {
        'count': Employee.count(),
        'page' : page
    }
    return render(request, 'site.html',context)

@api_view(['GET','POST'])

def employee_list(request):
    if request.method == 'GET':
        Employees = employee.objects.all()
        serializer = employeesSerializers(Employees, many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = employeesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        response = {
                "Status": True,
                "Status_code": status.HTTP_200_OK,
                "Status_Message": "Message",
                "Data": serializer.data
            }
        return Response(response, status=status.HTTP_200_OK)
            #return Response(serializer.data, status= status.HTTP_201_CREATED)

    
@api_view(['GET','PUT','DELETE'])

def employee_detail(request,id):
    try:
        emp = employee.objects.get(pk=id)
    except employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = employeesSerializers(emp)
        return Response(serializer.data)
    
    
    elif request.method == 'PUT':
        serializer = employeesSerializers(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    


    ##################################################################################################



@api_view(['GET','POST'])

def employee_role_list(request):
    if request.method == 'GET':
        Employees_role = employee_role.objects.all()
        serializer = employee_roleSerializers(Employees_role, many = True)
        #return JsonResponse({'employees': serializer.data})
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = employee_roleSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
@api_view(['GET','PUT','DELETE'])

def employee_role_detail(request,id):
    try:
        emp = employee_role.objects.get(pk=id)
    except employee_role.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = employee_roleSerializers(emp)
        return Response(serializer.data)
    
    
    elif request.method == 'PUT':
        serializer = employee_roleSerializers(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

#######################################################################################################


@api_view(['GET','POST'])

def employee_dept_list(request):
    if request.method == 'GET':
        Employees_role = employee_dept.objects.all()
        serializer = employee_deptSerializers(Employees_role, many = True)
        #return JsonResponse({'employees': serializer.data})
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = employee_deptSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
@api_view(['GET','PUT','DELETE'])

def employee_dept_detail(request,id):
    try:
        emp = employee_dept.objects.get(pk=id)
    except employee_dept.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = employee_deptSerializers(emp)
        return Response(serializer.data)
    
    
    elif request.method == 'PUT':
        serializer = employee_deptSerializers(emp, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        emp.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

##########################################################################################################


@api_view(['POST'])
def employee_filter(request):
    try:
        if request.method == 'POST':
            serializer = employee_filterSerializers(data=request.data)
            if serializer.is_valid():
                role = serializer.validated_data.get('employee_role')
                dept = serializer.validated_data.get('employee_dept')
                
                employees = employee.objects.all()
                
                if role:
                    employees = employees.filter(employee_role=role)
                
                if dept:
                    employees = employees.filter(employee_dept=dept)
                employee_data = employeesSerializers(employees, many=True).data
                
                response = {
                "Status": True,
                "Status_code": status.HTTP_200_OK,
                "Status_Message": "Message",
                "Data": employee_data
                }
                return Response(response, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

###########################################################################################################


@api_view(['GET','POST'])

def Branch_list(request):
    if request.method == 'GET':
        Employees = Branch.objects.all()
        serializer = BranchSerializers(Employees, many = True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = BranchSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
        response = {
                "Status": True,
                "Status_code": status.HTTP_200_OK,
                "Status_Message": "Message",
                "Data": serializer.data
            }
        return Response(response, status=status.HTTP_200_OK)
            #return Response(serializer.data, status= status.HTTP_201_CREATED)

    
@api_view(['GET','PUT','DELETE'])

def Branch_detail(request,id):
    try:
        bran = Branch.objects.get(pk=id)
    except Branch.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


    if request.method == 'GET':
        serializer = BranchSerializers(bran)
        return Response(serializer.data)
    
    
    elif request.method == 'PUT':
        serializer = BranchSerializers(bran, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    elif request.method == 'DELETE':
        bran.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

##############################################################################################################

@api_view(['GET','POST'])
def Branch_floor_list(request):
    if request.method == 'GET':
        branch = Branch_floor.objects.all()
        serializer = Branch_floorSerializers(branch,many = True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = Branch_floorSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
        response = {
                "Status": True,
                "Status_code": status.HTTP_200_OK,
                "Status_Message": "Message",
                "Data": serializer.data
            }
        return Response(response, status=status.HTTP_200_OK)
    
@api_view(['GET','PUT','DELETE'])
def Branch_floor_details(request,id):
    try:
        bran = Branch_floor.objects.get(pk = id)
    except Branch_floor.DoesNotExist:
        Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Branch_floorSerializers(bran)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Branch_floorSerializers(bran, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        bran.delete
        return Response(status=status.HTTP_204_NO_CONTENT) 
####################################################################################################################

@api_view(['GET','POST'])
def branch_employee_list(request):
    if request.method == 'GET':
        bran = Branch_employee.objects.all()
        serializer = Branch_employeeSerializers(bran , many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = Branch_employeeSerializers(data = request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "Status": True,
                "Status_code": status.HTTP_200_OK,
                "Status_Message": "Message",
                "Data": serializer.data
            }
        return Response(response, status=status.HTTP_200_OK)
@api_view(['GET','PUT','DELETE'])
def branch_employee_details(request,id):
    try:
        bran = Branch_employee.objects.get(pk = id)
    except Branch_employee.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = Branch_employeeSerializers(bran)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = Branch_employeeSerializers(bran,data = request.data)
        if serializer.is_valid:
            serializer.save()
            return Response(serializer.data())
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        bran.delete
        return Response(status=status.HTTP_204_NO_CONTENT)
    

@api_view(['POST'])
def branch_filter(request):
    try:
        if request.method == 'POST':
            serializer = Branch_filterSerializers(data=request.data)
            if serializer.is_valid():
                emp = serializer.validated_data.get('Branch_employees')
                floor = serializer.validated_data.get('Branch_floor')
                
                branch = Branch.objects.all()
                
                if emp:
                    employees = branch.filter(Branch_employees=emp)
                
                if floor:
                    floor = branch.filter(Branch_floor=floor)
                
                Branch_data = BranchSerializers(employees, many=True).data
                response = {
                "Status": True,
                "Status_code": status.HTTP_200_OK,
                "Status_Message": "Message",
                "Data": Branch_data
                }
                return Response(response, status=status.HTTP_200_OK)
            
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    except Branch.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    

###############################################################################################################


@api_view(['POST'])
def login_view(request):
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        email = serializer.validated_data['email']
        password = serializer.validated_data['password']
        print(email)
        print(password)

        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            user_data = employeesSerializers(user).data
            return Response(user_data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid credentials"}, status=status.HTTP_401_UNAUTHORIZED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)