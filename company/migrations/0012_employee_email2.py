# Generated by Django 5.0.6 on 2024-06-22 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0011_rename_branch_details_branch_branch_floor'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email2',
            field=models.EmailField(default=10, max_length=100),
            preserve_default=False,
        ),
    ]
