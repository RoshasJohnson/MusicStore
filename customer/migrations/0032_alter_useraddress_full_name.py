# Generated by Django 4.0 on 2022-01-31 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0031_alter_useraddress_options_alter_useraddress_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraddress',
            name='full_name',
            field=models.CharField(max_length=200),
        ),
    ]
