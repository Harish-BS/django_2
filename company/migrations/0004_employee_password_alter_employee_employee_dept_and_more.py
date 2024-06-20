# Generated by Django 5.0.6 on 2024-06-20 09:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_employee_employee_dept_employee_employee_role_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='password',
            field=models.CharField(default='guest', max_length=20),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_dept',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.employee_dept'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='employee_role',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.employee_role'),
        ),
    ]