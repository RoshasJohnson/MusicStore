# Generated by Django 4.0 on 2022-01-15 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0005_alter_useraddress_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categorys',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
