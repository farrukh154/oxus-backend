# Generated by Django 4.1.2 on 2024-03-25 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('request_credit', '0028_requestcredit_approve_currency_new_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestcredit',
            name='approve_currency',
        ),
        migrations.RemoveField(
            model_name='requestcredit',
            name='currency',
        ),
    ]
