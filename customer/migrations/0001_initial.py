# Generated by Django 4.1.2 on 2024-05-02 19:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('division', '0008_alter_currencyexchange_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='updated')),
                ('name', models.CharField(default='', max_length=255, verbose_name='name')),
                ('birthday', models.DateField(blank=True, null=True, verbose_name='birthday')),
                ('gender', models.CharField(blank=True, choices=[('male', 'Мард'), ('female', 'Зан')], max_length=50, null=True, verbose_name='gender')),
                ('client_ID', models.BigIntegerField(blank=True, null=True, verbose_name='Client ID')),
                ('INN', models.CharField(blank=True, default='', max_length=9, null=True, unique=True, validators=[django.core.validators.MinLengthValidator(9)], verbose_name='INN')),
                ('passport', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Passport')),
                ('passport_date', models.DateField(blank=True, null=True, verbose_name='passport_date')),
                ('passport_details', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Passport details')),
                ('registration_address_street', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='registration address street')),
                ('address_street', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='address street')),
                ('phone1', models.CharField(blank=True, default='', max_length=15, null=True, verbose_name='phone 1')),
                ('phone2', models.CharField(blank=True, default='', max_length=15, null=True, verbose_name='phone 2')),
                ('family_status', models.CharField(blank=True, choices=[('married', 'Оиладор'), ('single', 'Мучаррад'), ('separated', 'Чудошуда'), ('widow', 'Бевазан/Мард')], max_length=50, null=True, verbose_name='family status')),
                ('spouse', models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='spouse')),
                ('spouse_phone', models.CharField(blank=True, default='', max_length=15, null=True, verbose_name='spouse phone')),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='customer_address', to='division.district', verbose_name='address')),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='division.branch')),
                ('registration_address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='customer_registration_address', to='division.district', verbose_name='registration address')),
            ],
            options={
                'verbose_name': 'customers',
                'verbose_name_plural': 'customers',
            },
        ),
    ]
