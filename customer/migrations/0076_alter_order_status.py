# Generated by Django 4.0 on 2022-02-14 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0075_usercreation_coupen_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Canceled', 'Canceled'), ('Delivered', 'Delivered'), ('Packed', 'Packed'), ('Return', 'Return')], default='Processing', max_length=100),
        ),
    ]
