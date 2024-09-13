# Generated by Django 4.1.2 on 2023-12-06 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request_credit', '0004_remove_cibthistory_user_cibthistory_created_by_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requestcredit',
            old_name='Passport_ID',
            new_name='passport',
        ),
        migrations.AddField(
            model_name='requestcredit',
            name='credit_ID',
            field=models.CharField(blank=True, default='', max_length=32, null=True, verbose_name='credit account'),
        ),
    ]
