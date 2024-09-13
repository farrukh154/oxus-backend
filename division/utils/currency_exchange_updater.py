import requests
from xml.etree import ElementTree as ET
from datetime import datetime
from division.models.currency_exchange import CurrencyExchange
from division.models.currency import Currency
from django.db import transaction

def currency_exchange_updater(currencies_to_sync):
    def format_date(date):
        return date.strftime('%Y-%m-%d')
    
    base_url = 'https://www.nbt.tj/tj/kurs/export_xml_dynamic.php'
    end_date = datetime.now()
    start_date = datetime(2005, 1, 1) # Начальная дата для поиска данных на сайте
    exchanges_to_create = []

    url = f"{base_url}?d1={format_date(start_date)}&d2={format_date(end_date)}&cs={currencies_to_sync}&export=xml"
    response = requests.get(url)

    if response.status_code == 200:
        root = ET.fromstring(response.content)

        for record in root.findall('.//Record'):
            date_str = record.get('Date')
            charcode = record.find('CharCode').text
            rate = record.find('Value').text
            date = datetime.strptime(date_str, '%d.%m.%Y')

            currency_from_code = 'TJS'
            currency_from = Currency.objects.get(code=currency_from_code)
            currency_to_obj = Currency.objects.get(code=charcode)

            if not CurrencyExchange.objects.filter(date=date, currency_from=currency_from, currency_to=currency_to_obj).exists():
                exchange = CurrencyExchange(rate=rate, date=date, currency_from=currency_from, currency_to=currency_to_obj)
                exchanges_to_create.append(exchange)
                
    else:
        print(f"Ошибка при получении данных: {response.status_code}")

    with transaction.atomic():
        CurrencyExchange.objects.bulk_create(exchanges_to_create, ignore_conflicts=True)
