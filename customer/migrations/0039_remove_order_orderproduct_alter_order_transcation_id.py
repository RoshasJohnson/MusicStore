# Generated by Django 4.0 on 2022-02-03 14:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0038_rename_product_order_orderproduct'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='orderproduct',
        ),
        migrations.AlterField(
            model_name='order',
            name='transcation_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
