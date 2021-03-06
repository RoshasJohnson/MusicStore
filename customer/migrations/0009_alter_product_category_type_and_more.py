# Generated by Django 4.0 on 2022-01-15 14:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0008_product_stock_alter_product_category_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_description',
            field=models.CharField(max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_name',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_prize',
            field=models.FloatField(max_length=200, null=True),
        ),
    ]
