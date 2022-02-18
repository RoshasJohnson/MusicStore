# Generated by Django 4.0 on 2022-02-17 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0085_alter_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='date_delivered',
            field=models.DateField(default='2022-01-01'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Return', 'Return'), ('Packed', 'Packed'), ('Delivered', 'Delivered'), ('Canceled', 'Canceled')], default='Processing', max_length=100),
        ),
    ]
