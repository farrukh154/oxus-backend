# Generated by Django 4.1.2 on 2024-05-01 12:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reports', '0017_alter_report_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='report',
            options={'permissions': (('report-abacus-olb-per-loan_report', 'Report: Abacus OLB per loans'), ('report-abacus-active-loan_report', 'Report: Abacus Active loans'), ('report-swift-loan_report', 'Report: Swift loans'), ('report-swift-loan-break_report', 'Report: Swift loans break down'), ('report-abacus-swift-loan_report', 'Report: Abacus client list for Swift loan'), ('report-abacus-llp-per-loan_report', 'Report: Abacus OLB and LLP per loans'), ('report-abacus-disbursement_report', 'Report: Abacus disbursement')), 'verbose_name': 'Reports', 'verbose_name_plural': 'Reports'},
        ),
    ]
