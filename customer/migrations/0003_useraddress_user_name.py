# Generated by Django 4.0 on 2022-01-15 03:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_product_useraddress'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraddress',
            name='user_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.usercreation'),
        ),
    ]
