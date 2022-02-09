# Generated by Django 4.0 on 2022-02-08 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0065_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Packed', 'Packed'), ('Delivered', 'Delivered'), ('Canceled', 'Canceled'), ('Accepted', 'Accepted'), ('On the way', 'On the way'), ('Return', 'Return')], default='Processing', max_length=100),
        ),
    ]
