# Generated by Django 4.1.2 on 2024-04-17 13:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoring', '0003_crif_parent_crif_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='crif',
            old_name='credit_id',
            new_name='abacus_account_number',
        ),
    ]
