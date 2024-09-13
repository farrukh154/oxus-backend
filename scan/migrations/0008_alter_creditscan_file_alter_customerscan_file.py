# Generated by Django 4.1.2 on 2024-04-24 21:45

import common.fields.UploadFileFields
from django.db import migrations
import scan.models.credit_scan.model
import scan.models.customer_scan.model
import scan.utils.utils


class Migration(migrations.Migration):

    dependencies = [
        ('scan', '0007_alter_creditscan_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditscan',
            name='file',
            field=common.fields.UploadFileFields.UploadFileField(upload_to=scan.models.credit_scan.model.get_credit_scan_path, validators=[scan.utils.utils.only_pdf], verbose_name='File'),
        ),
        migrations.AlterField(
            model_name='customerscan',
            name='file',
            field=common.fields.UploadFileFields.UploadFileField(upload_to=scan.models.customer_scan.model.get_customer_scan_path, validators=[scan.utils.utils.only_pdf], verbose_name='file'),
        ),
    ]
