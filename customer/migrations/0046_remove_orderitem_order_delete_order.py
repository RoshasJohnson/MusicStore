# Generated by Django 4.0 on 2022-02-03 15:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0045_remove_order_payment_method'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='order',
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]
