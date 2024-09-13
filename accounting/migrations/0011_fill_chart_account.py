# Generated by Django 4.1.2 on 2024-08-16 13:28

from django.db import migrations

def fill_chart_account(apps, schema_editor):
    ChartAccount = apps.get_model('accounting', 'ChartAccount')
    
    initial_data = [
        {
            "name": "ASSETS",
            "ru_name": "АКТИВЫ",
            "tj_name": "ДОРОИЦО",
            "account_number": "10000",
        },
        {
            "name": "CASH AND OTHER CASH DOCUMENTS",
            "ru_name": "НАЛИЧНОСТЬ И ПРОЧИЕ КАССОВЫЕ ДОКУМЕНТЫ",
            "tj_name": "ПУЛИ НАҚД ВА ДИГАР ЦУҶҶАТЦОИ КАССА",
            "account_number": "10100",
        },
        {
            "name": "Cash - national currency",
            "ru_name": "НАЛИЧНОСТЬ И ПРОЧИЕ КАССОВЫЕ ДОКУМЕНТЫ",
            "tj_name": "ПУЛИ НАҚД ВА ДИГАР ЦУҶҶАТЦОИ КАССА",
            "account_number": "10100",
        },
    ]
    
    for data in initial_data:
        ChartAccount.objects.create(**data)

class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0010_chartaccount_account_number'),
    ]

    operations = [
        migrations.RunPython(fill_chart_account),
    ]
