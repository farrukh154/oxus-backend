# Generated by Django 4.1.2 on 2023-12-20 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request_credit', '0017_requestcredit_approve_amount_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestcredit',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Мард'), ('female', 'Зан')], max_length=50, null=True, verbose_name='gender'),
        ),
    ]
