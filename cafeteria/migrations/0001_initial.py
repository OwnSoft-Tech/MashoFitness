# Generated by Django 4.0.1 on 2022-03-01 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='addItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_code', models.IntegerField()),
                ('item_name', models.CharField(max_length=50)),
                ('item_unit', models.CharField(max_length=30)),
                ('item_category', models.CharField(max_length=30)),
                ('item_brand', models.CharField(max_length=30)),
                ('item_manufacturer', models.CharField(max_length=30)),
                ('item_selling_price', models.IntegerField()),
                ('item_max_selling_quantity', models.IntegerField()),
                ('item_min_selling_quantity', models.IntegerField()),
                ('item_reorder_level', models.IntegerField()),
                ('item_image', models.ImageField(upload_to='items_images/')),
                ('search_tag', models.CharField(max_length=50)),
                ('item_description', models.CharField(max_length=100)),
                ('item_status', models.CharField(max_length=20)),
                ('item_expiry', models.DateField()),
            ],
        ),
    ]
