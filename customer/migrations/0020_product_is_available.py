# Generated by Django 4.0 on 2022-01-22 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0019_alter_product_stock'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_available',
            field=models.BooleanField(default=True),
        ),
    ]
