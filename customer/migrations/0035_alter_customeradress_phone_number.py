# Generated by Django 4.0 on 2022-02-01 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0034_alter_customeradress_phone_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customeradress',
            name='phone_number',
            field=models.IntegerField(),
        ),
    ]
