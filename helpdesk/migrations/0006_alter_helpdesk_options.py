# Generated by Django 4.1.2 on 2024-03-23 21:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('helpdesk', '0005_auto_20240218_1711'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='helpdesk',
            options={'permissions': [('can-view-all_helpdesk', 'Can view all helpdesks')], 'verbose_name': 'helpdesk', 'verbose_name_plural': 'helpdesk'},
        ),
    ]