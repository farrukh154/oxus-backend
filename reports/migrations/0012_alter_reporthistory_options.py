# Generated by Django 4.1.2 on 2024-03-14 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0011_remove_report_permission_name'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reporthistory',
            options={'verbose_name': 'report history', 'verbose_name_plural': 'report histories'},
        ),
    ]
