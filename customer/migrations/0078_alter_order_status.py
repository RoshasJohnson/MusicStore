# Generated by Django 4.0 on 2022-02-14 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0077_alter_order_status_wishlist_offer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Return', 'Return'), ('Canceled', 'Canceled'), ('Delivered', 'Delivered'), ('Packed', 'Packed')], default='Processing', max_length=100),
        ),
    ]
