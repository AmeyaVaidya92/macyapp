# Generated by Django 3.2.3 on 2021-08-29 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_orders_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orders',
            old_name='item_json',
            new_name='items_json',
        ),
    ]
