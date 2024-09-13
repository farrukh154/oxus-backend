# Generated by Django 4.1.2 on 2024-08-13 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0002_chartaccount'),
    ]

    operations = [
        migrations.AddField(
            model_name='chartaccount',
            name='ru_name',
            field=models.CharField(default='default_ru_name', max_length=100),
        ),
        migrations.AddField(
            model_name='chartaccount',
            name='tj_name',
            field=models.CharField(default='default_tj_name', max_length=100),
        ),
    ]
