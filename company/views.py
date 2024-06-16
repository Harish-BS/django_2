from django.http import HttpResponse
from django.shortcuts import render


from .models import employee
from .serializers import employeesSerializers
from django.http import JsonResponse
from rest_framework.decorators import api_view 
from rest_framework.response import Response 
from rest_framework import status 
from .models import employee_role
from .models import employee_dept
from .serializers import employee_roleSerializers
from .serializers import employee_deptSerializers


@api_view(['GET','POST'])

def employee_list(request):
    if request.method == 'GET':
        Employees = employee.objects.all()
        serializer = employeesSerializers(Employees, many = True)
        #return JsonResponse({'employees': serializer.data})
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = employeesSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        
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
