# Generated by Django 4.0 on 2022-02-03 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0055_order_user_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total_prize',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]