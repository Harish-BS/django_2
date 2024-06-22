"""
URL configuration for company project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from company import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('employee/', views.employee_list),
    path('employee/<int:id>', views.employee_detail),
    path('employee_role/', views.employee_role_list),
    path('employee_role/<int:id>', views.employee_role_detail),
    path('employee_dept/', views.employee_dept_list),
    path('employee_dept/<int:id>', views.employee_dept_detail),
    path('employee/filter/',views.employee_filter),
    path('branch/',views.Branch_list),
    path('branch/<int:id>',views.Branch_detail),
    path('branch_floor/', views.Branch_floor_list),
    path('branch_floor/<int:id>',views.Branch_floor_details),
    path('branch_employee/', views.branch_employee_list),
    path('branch_employee/<int:id>',views.branch_employee_details),
    path('branch/filter/',views.branch_filter),
    path('login/',views.login_view)
]