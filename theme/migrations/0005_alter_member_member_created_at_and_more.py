# Generated by Django 4.0.1 on 2022-02-15 11:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0004_alter_member_member_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='member_created_at',
            field=models.DateField(default=datetime.datetime(2022, 2, 15, 16, 27, 42, 698730)),
        ),
        migrations.AlterField(
            model_name='member',
            name='member_membership_expiry_date',
            field=models.DateField(default=datetime.datetime(2022, 2, 15, 16, 27, 42, 698730)),
        ),
        migrations.AlterField(
            model_name='membershipcategory',
            name='category_created_at',
            field=models.DateField(default=datetime.datetime(2022, 2, 15, 16, 27, 42, 697732)),
        ),
        migrations.AlterField(
            model_name='payment',
            name='payment_created_at',
            field=models.DateField(default=datetime.datetime(2022, 2, 15, 16, 27, 42, 698730)),
        ),
    ]
