# Generated by Django 4.1.2 on 2024-03-14 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('division', '0004_currencyexchange'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currencyexchange',
            name='currency_from',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currency_from', to='division.currency'),
        ),
        migrations.AlterField(
            model_name='currencyexchange',
            name='currency_to',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='currency_to', to='division.currency'),
        ),
        migrations.AlterField(
            model_name='currencyexchange',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='currencyexchange',
            name='rate',
            field=models.DecimalField(blank=True, decimal_places=4, max_digits=12, null=True, verbose_name='rate'),
        ),
    ]
