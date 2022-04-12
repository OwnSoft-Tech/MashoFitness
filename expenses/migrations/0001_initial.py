# Generated by Django 4.0.1 on 2022-04-12 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='expensesData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('account_head', models.CharField(max_length=20)),
                ('paid_amount', models.IntegerField()),
                ('payment_mode', models.CharField(max_length=30)),
                ('expenses_for', models.CharField(max_length=20)),
                ('receipent_name', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=200)),
                ('comments', models.CharField(max_length=200)),
            ],
        ),
    ]
