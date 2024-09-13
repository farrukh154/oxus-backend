# Generated by Django 4.2.5 on 2023-11-30 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Terminal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='updated')),
                ('name', models.CharField(default='', max_length=255, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'terminal',
                'verbose_name_plural': 'terminals',
            },
        ),
        migrations.CreateModel(
            name='Terminal_Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='updated')),
                ('name', models.CharField(default='', max_length=255, unique=True, verbose_name='name')),
            ],
            options={
                'verbose_name': 'terminal vendor',
                'verbose_name_plural': 'terminal vendors',
            },
        ),
    ]