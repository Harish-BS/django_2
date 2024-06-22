# Generated by Django 5.0.6 on 2024-06-22 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0013_alter_employee_email2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='email2',
        ),
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]