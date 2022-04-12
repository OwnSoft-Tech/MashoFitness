# Generated by Django 4.0.1 on 2022-04-12 08:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployeeRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_contact', models.CharField(max_length=12)),
                ('employee_image', models.ImageField(upload_to='profile_images/')),
                ('employee_cnic', models.CharField(blank=True, max_length=15, null=True)),
                ('employee_address', models.CharField(blank=True, max_length=200, null=True)),
                ('employee_gender', models.CharField(max_length=10)),
                ('employee_dob', models.DateField(null=True)),
                ('employee_age', models.IntegerField(null=True)),
                ('employee_blood_group', models.CharField(max_length=10, null=True)),
                ('employee_type', models.CharField(max_length=30)),
                ('employee_pay', models.IntegerField(default=0)),
                ('employee_status', models.CharField(max_length=20)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
