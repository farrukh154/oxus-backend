# Generated by Django 4.1.2 on 2024-02-12 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request_credit', '0022_cibthistory_credit_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='cibthistory',
            name='client_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='Клиент Id'),
        ),
        migrations.AlterField(
            model_name='cibthistory',
            name='credit_id',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Кредит Id'),
        ),
    ]
