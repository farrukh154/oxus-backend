# Generated by Django 4.1.2 on 2024-07-22 21:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_customer_phone3'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customer',
            options={'verbose_name': 'customer', 'verbose_name_plural': 'customers'},
        ),
    ]
