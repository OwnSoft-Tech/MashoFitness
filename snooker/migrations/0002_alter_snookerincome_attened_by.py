# Generated by Django 3.2 on 2022-04-04 22:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_alter_employeerecord_employee_password'),
        ('snooker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snookerincome',
            name='attened_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='attened_by', to='employees.employeerecord'),
        ),
    ]