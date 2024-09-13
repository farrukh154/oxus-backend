# Generated by Django 4.1.2 on 2024-07-12 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('division', '0008_alter_currencyexchange_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='uid',
            field=models.CharField(blank=True, help_text='Unique identifier for reference to record from code. Do not change if set!', max_length=100, null=True, unique=True),
        ),
    ]
