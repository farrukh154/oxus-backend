# Generated by Django 4.1.2 on 2024-01-28 17:49

from django.db import migrations, models
import users.models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_user_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_signature',
            field=models.FileField(blank=True, null=True, upload_to=users.models.get_signature_scan_path, verbose_name='User scan signature'),
        ),
    ]
