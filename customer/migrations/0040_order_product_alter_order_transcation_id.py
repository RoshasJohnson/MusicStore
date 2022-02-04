# Generated by Django 4.0 on 2022-02-03 14:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0039_remove_order_orderproduct_alter_order_transcation_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='customer.product'),
        ),
        migrations.AlterField(
            model_name='order',
            name='transcation_id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]