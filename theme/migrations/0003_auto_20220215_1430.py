# Generated by Django 3.2 on 2022-02-15 09:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0002_auto_20220212_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_created_at',
            field=models.DateField(default=datetime.datetime(2022, 2, 15, 14, 30, 57, 798773)),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_membership_expiry_date',
            field=models.DateField(default=datetime.datetime(2022, 2, 15, 14, 30, 57, 798773)),
        ),
        migrations.AlterField(
            model_name='membershipcategory',
            name='category_created_at',
            field=models.DateField(default=datetime.datetime(2022, 2, 15, 14, 30, 57, 798773)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_created_at',
            field=models.DateField(default=datetime.datetime(2022, 2, 15, 14, 30, 57, 798773)),
        ),
    ]
