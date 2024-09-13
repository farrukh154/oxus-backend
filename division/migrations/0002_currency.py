# Generated by Django 4.1.2 on 2024-03-04 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('division', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='updated')),
                ('uid', models.CharField(blank=True, help_text='Unique identifier for reference to record from code. Do not change if set!', max_length=30, null=True, unique=True)),
                ('name', models.CharField(default='', max_length=255, verbose_name='name')),
                ('code', models.CharField(default='', max_length=255, verbose_name='code')),
                ('description', models.CharField(default='', max_length=255, verbose_name='description')),
            ],
            options={
                'verbose_name': 'currency',
                'verbose_name_plural': 'currencies',
            },
        ),
    ]
