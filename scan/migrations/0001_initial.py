# Generated by Django 4.1.2 on 2024-03-12 08:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerScan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='updated')),
                ('file', models.FileField(upload_to='uploads/')),
                ('created_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='created by')),
                ('updated_by', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='updated by')),
            ],
            options={
                'verbose_name': 'customer scans',
                'verbose_name_plural': 'customer scans',
            },
        ),
    ]
