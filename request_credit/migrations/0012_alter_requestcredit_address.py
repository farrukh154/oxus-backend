# Generated by Django 4.1.2 on 2023-12-08 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('division', '0001_initial'),
        ('request_credit', '0011_requestcredit_acted_requestcredit_current_debt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestcredit',
            name='address',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='address', to='division.district', verbose_name='address'),
        ),
    ]
