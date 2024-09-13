# Generated by Django 4.1.2 on 2024-08-16 10:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0007_alter_account_code_alter_account_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='code',
            field=models.TextField(max_length=100, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='account',
            name='description',
            field=models.TextField(max_length=350, verbose_name='Description'),
        ),
    ]