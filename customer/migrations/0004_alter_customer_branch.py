# Generated by Django 4.1.2 on 2024-07-24 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('division', '0010_auto_20240715_1235'),
        ('customer', '0003_alter_customer_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='branch',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='division.branch', verbose_name='branch'),
        ),
    ]
