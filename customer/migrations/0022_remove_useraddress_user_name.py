# Generated by Django 4.0 on 2022-01-25 04:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0021_cart_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useraddress',
            name='user_name',
        ),
    ]
