# Generated by Django 4.0 on 2022-02-07 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0063_alter_order_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('On the way', 'On the way'), ('Canceled', 'Canceled'), ('Accepted', 'Accepted'), ('Packed', 'Packed'), ('Return', 'Return'), ('Delivered', 'Delivered')], default='Pending', max_length=100),
        ),
    ]