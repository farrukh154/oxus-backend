# Generated by Django 4.1.2 on 2024-03-14 13:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('division', '0002_currency'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyExchange',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='updated')),
                ('date', models.DateField(blank=True, null=True, verbose_name='date')),
                ('rate', models.DecimalField(blank=True, decimal_places=2, max_digits=12, null=True, verbose_name='rate')),
                ('currency_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='currency_from', to='division.currency')),
                ('currency_to', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='currency_to', to='division.currency')),
            ],
            options={
                'verbose_name': 'currency Exchange',
                'verbose_name_plural': 'currency exchanges',
            },
        ),
    ]
