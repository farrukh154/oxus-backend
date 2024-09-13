# Generated by Django 4.1.2 on 2024-03-18 18:28

from django.db import migrations, models
import scan.models.customer_scan.model


class Migration(migrations.Migration):

    dependencies = [
        ('scan', '0003_alter_customerscantype_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerscan',
            name='abacus_id',
            field=models.IntegerField(blank=True, null=True, verbose_name='abacus_ID'),
        ),
        migrations.AlterField(
            model_name='customerscan',
            name='file',
            field=models.FileField(upload_to=scan.models.customer_scan.model.get_customer_scan_path, verbose_name='file'),
        ),
    ]