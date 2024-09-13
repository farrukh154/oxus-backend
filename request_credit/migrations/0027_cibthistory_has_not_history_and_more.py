# Generated by Django 4.1.2 on 2024-02-20 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request_credit', '0026_alter_requestcredit_education'),
    ]

    operations = [
        migrations.AddField(
            model_name='cibthistory',
            name='has_not_history',
            field=models.BooleanField(default=True, verbose_name='has not history'),
        ),
        migrations.AlterField(
            model_name='requestcredit',
            name='education_info',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='education info'),
        ),
    ]