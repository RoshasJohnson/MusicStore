# Generated by Django 4.0 on 2022-01-31 10:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0030_alter_useraddress_options_alter_useraddress_table'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='useraddress',
            options={'managed': True, 'verbose_name': 'useradress', 'verbose_name_plural': 'useradresss'},
        ),
        migrations.AlterModelTable(
            name='useraddress',
            table='',
        ),
    ]