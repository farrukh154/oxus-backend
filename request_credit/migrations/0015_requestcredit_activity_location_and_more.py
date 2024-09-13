# Generated by Django 4.1.2 on 2023-12-09 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request_credit', '0014_requestcredit_credit_purpose_requestcredit_currency_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestcredit',
            name='activity_location',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='address of location of activity'),
        ),
        migrations.AddField(
            model_name='requestcredit',
            name='client_capital',
            field=models.IntegerField(blank=True, null=True, verbose_name='client capital'),
        ),
        migrations.AddField(
            model_name='requestcredit',
            name='client_capital_info',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='client capital info'),
        ),
        migrations.AddField(
            model_name='requestcredit',
            name='monthly_household_expenses',
            field=models.IntegerField(blank=True, null=True, verbose_name='monthly household expenses'),
        ),
        migrations.AddField(
            model_name='requestcredit',
            name='monthly_household_expenses_info',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='monthly household expenses info'),
        ),
        migrations.AddField(
            model_name='requestcredit',
            name='monthly_income',
            field=models.IntegerField(blank=True, null=True, verbose_name='monthly income'),
        ),
        migrations.AddField(
            model_name='requestcredit',
            name='monthly_income_info',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='monthly income info'),
        ),
        migrations.AddField(
            model_name='requestcredit',
            name='monthly_payment_loans',
            field=models.IntegerField(blank=True, null=True, verbose_name='monthly payment loans'),
        ),
        migrations.AddField(
            model_name='requestcredit',
            name='monthly_payment_loans_info',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='monthly payment loans info'),
        ),
        migrations.AddField(
            model_name='requestcredit',
            name='monthly_profit_info',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='monthly profit info'),
        ),
        migrations.AddField(
            model_name='requestcredit',
            name='total_business_assets',
            field=models.IntegerField(blank=True, null=True, verbose_name='total business assets'),
        ),
        migrations.AddField(
            model_name='requestcredit',
            name='total_business_assets_info',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='total business assets info'),
        ),
        migrations.AddField(
            model_name='requestcredit',
            name='total_household_assets',
            field=models.IntegerField(blank=True, null=True, verbose_name='total household assets'),
        ),
        migrations.AddField(
            model_name='requestcredit',
            name='total_household_assets_info',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='total household assets info'),
        ),
    ]
