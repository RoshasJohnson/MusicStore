# Generated by Django 4.0 on 2022-01-16 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0010_product_product_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_image',
            field=models.FileField(blank=True, null=True, upload_to='images/'),
        ),
    ]