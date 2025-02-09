# Generated by Django 4.1.2 on 2024-07-29 18:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customer', '0004_alter_customer_branch'),
        ('division', '0010_auto_20240715_1235'),
        ('request_credit', '0042_alter_requestcredit_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestcredit',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='division.branch', verbose_name='branch'),
        ),
        migrations.AlterField(
            model_name='requestcredit',
            name='current_debt',
            field=models.CharField(blank=True, choices=[('yes', 'Ха'), ('no', 'Не')], max_length=50, null=True, verbose_name='current debt'),
        ),
        migrations.AlterField(
            model_name='requestcredit',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='customer.customer', verbose_name='customer'),
        ),
        migrations.AlterField(
            model_name='requestcredit',
            name='decision_client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='request_credit.clientdecision', verbose_name='decision client'),
        ),
        migrations.AlterField(
            model_name='requestcredit',
            name='status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='request_credit', to='request_credit.requeststatus', verbose_name='status'),
        ),
        migrations.AlterField(
            model_name='requestcredit',
            name='status_change_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='request_credit', to=settings.AUTH_USER_MODEL, verbose_name='status change by'),
        ),
        migrations.AlterField(
            model_name='requestcredit',
            name='underwriter_status',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='underwriter_request_credit', to='request_credit.requeststatus', verbose_name='underwriter status'),
        ),
        migrations.AlterField(
            model_name='requestcredit',
            name='underwriter_status_change_by',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='underwriter_request_credit', to=settings.AUTH_USER_MODEL, verbose_name='underwriter status change by'),
        ),
    ]
