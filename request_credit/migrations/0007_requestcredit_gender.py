# Generated by Django 4.1.2 on 2023-12-08 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request_credit', '0006_remove_requestcredit_date_requestcredit_birthdate'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestcredit',
            name='gender',
            field=models.CharField(blank=True, choices=[('male', 'Муж'), ('female', 'Жен')], max_length=50, null=True, verbose_name='smart loan role'),
        ),
    ]
