# Generated by Django 4.0 on 2022-02-14 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0084_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Delivered', 'Delivered'), ('Packed', 'Packed'), ('Canceled', 'Canceled'), ('Return', 'Return')], default='Processing', max_length=100),
        ),
    ]
