# Generated by Django 4.0 on 2022-02-10 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0073_remove_category_coupen_offer_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Return', 'Return'), ('Packed', 'Packed'), ('Canceled', 'Canceled'), ('Delivered', 'Delivered')], default='Processing', max_length=100),
        ),
    ]
