# Generated by Django 4.0 on 2022-02-03 16:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0051_alter_order_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='order_product',
        ),
    ]
