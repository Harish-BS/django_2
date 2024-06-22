# Generated by Django 5.0.6 on 2024-06-21 20:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_branch_branch_details_branch_branch_employees_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Branch_detail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor', models.IntegerField(null=True, verbose_name=100)),
            ],
        ),
        migrations.CreateModel(
            name='Branch_employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_nos', models.IntegerField(null=True, verbose_name=10000)),
            ],
        ),
        migrations.AlterField(
            model_name='branch',
            name='Branch_details',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.branch_detail'),
        ),
        migrations.AlterField(
            model_name='branch',
            name='Branch_employees',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='company.branch_employee'),
        ),
        migrations.DeleteModel(
            name='Branch_details',
        ),
        migrations.DeleteModel(
            name='Branch_employees',
        ),
    ]
