# Generated by Django 4.2.2 on 2023-06-19 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_product_product_arrival_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_arrival_status',
            field=models.CharField(default='new', max_length=50),
        ),
    ]
