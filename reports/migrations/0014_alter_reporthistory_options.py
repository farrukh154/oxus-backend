# Generated by Django 4.1.2 on 2024-03-23 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0013_reporthistory_duration_reporthistory_xlsx_report_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reporthistory',
            options={'permissions': (('can-view-all-generated-report_reporthistory', 'Can view all generated report by other user'),), 'verbose_name': 'report history', 'verbose_name_plural': 'report histories'},
        ),
    ]
