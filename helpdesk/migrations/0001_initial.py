# Generated by Django 4.2.5 on 2023-11-30 08:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Helpdesk_Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='updated')),
                ('uid', models.CharField(blank=True, help_text='Unique identifier for reference to record from code. Do not change if set!', max_length=30, null=True, unique=True)),
                ('name', models.CharField(default='', max_length=255, verbose_name='name')),
            ],
            options={
                'verbose_name': 'helpdesk branch',
                'verbose_name_plural': 'helpdesk branches',
            },
        ),
        migrations.CreateModel(
            name='Helpdesk_Priority',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='updated')),
                ('uid', models.CharField(blank=True, help_text='Unique identifier for reference to record from code. Do not change if set!', max_length=30, null=True, unique=True)),
                ('name', models.CharField(default='', max_length=255, verbose_name='name')),
            ],
            options={
                'verbose_name': 'helpdesk priority',
                'verbose_name_plural': 'helpdesk priorities',
            },
        ),
        migrations.CreateModel(
            name='Helpdesk_Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='updated')),
                ('uid', models.CharField(blank=True, help_text='Unique identifier for reference to record from code. Do not change if set!', max_length=30, null=True, unique=True)),
                ('name', models.CharField(default='', max_length=255, verbose_name='name')),
            ],
            options={
                'verbose_name': 'helpdesk status',
                'verbose_name_plural': 'helpdesk statuses',
            },
        ),
        migrations.CreateModel(
            name='Helpdesk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, null=True, verbose_name='created')),
                ('updated', models.DateTimeField(auto_now=True, null=True, verbose_name='updated')),
                ('name', models.CharField(default='', max_length=255, verbose_name='name')),
                ('branch', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='helpdesk.helpdesk_branch')),
                ('priority', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='helpdesk.helpdesk_priority')),
                ('status', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='helpdesk.helpdesk_status')),
            ],
            options={
                'verbose_name': 'helpdesk',
                'verbose_name_plural': 'helpdesk',
            },
        ),
    ]
