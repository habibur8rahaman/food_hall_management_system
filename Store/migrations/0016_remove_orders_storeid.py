# Generated by Django 4.2.4 on 2023-08-20 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Store', '0015_orders_storeid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='storeID',
        ),
    ]
