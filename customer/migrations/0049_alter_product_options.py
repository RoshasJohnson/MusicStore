# Generated by Django 4.0 on 2022-02-03 15:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0048_rename_products_orderitem_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'managed': True, 'verbose_name': 'Products', 'verbose_name_plural': 'Products'},
        ),
    ]
