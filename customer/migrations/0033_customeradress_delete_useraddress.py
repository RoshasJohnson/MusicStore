# Generated by Django 4.0 on 2022-02-01 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0032_alter_useraddress_full_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerAdress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField(max_length=15)),
                ('house_name', models.CharField(max_length=200, null=True)),
                ('street_name', models.CharField(max_length=200, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('state', models.CharField(max_length=200, null=True)),
                ('country', models.CharField(max_length=200, null=True)),
                ('post_code', models.IntegerField(max_length=200, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.usercreation')),
            ],
            options={
                'verbose_name': 'CustomerAdress',
                'verbose_name_plural': 'CustomerAdress',
                'db_table': '',
                'managed': True,
            },
        ),
        migrations.DeleteModel(
            name='useraddress',
        ),
    ]