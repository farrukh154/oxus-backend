# Generated by Django 4.1.2 on 2024-08-07 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_alter_user_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='full name'),
        ),
    ]
