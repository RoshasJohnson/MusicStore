# Generated by Django 4.0 on 2022-02-03 15:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0046_remove_orderitem_order_delete_order'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='product',
            new_name='products',
        ),
    ]
